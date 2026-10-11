"""Functii comune pentru Lab6 pe PYNQ-Z2 (PYNQ 2.7).

Procesarea CPU functioneaza separat; calea hibrida necesita perechea
resizer.bit/resizer.hwh din Lab5. Nu se pretinde existenta Sobel in PL.
"""
from pathlib import Path
from time import perf_counter, sleep
import numpy as np
import cv2


LAB_DIR = Path(__file__).resolve().parent
DEFAULT_IMAGE = LAB_DIR.parent / "Lab4" / "images" / "fruits.jpg"


def load_test_image(path=DEFAULT_IMAGE):
    """Incarca imaginea BGR uint8 folosita in Lab4."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            "Imaginea lipseste: {}. Copiati intregul repository "
            "Edge-Computing, inclusiv Lab4/images/.".format(path)
        )
    frame = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if frame is None:
        raise RuntimeError("OpenCV nu poate citi imaginea: {}".format(path))
    return frame


def sobel_software(gray, border_type=cv2.BORDER_DEFAULT):
    """Referinta Sobel L2 din Lab4, cu aceeasi tratare a marginilor."""
    gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3,
                   borderType=border_type)
    gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3,
                   borderType=border_type)
    return cv2.convertScaleAbs(cv2.magnitude(gx, gy))


def process_cpu(image_bgr, size):
    """Resize biliniar, grayscale si Sobel, integral pe ARM."""
    small = cv2.resize(image_bgr, size, interpolation=cv2.INTER_LINEAR)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    return sobel_software(gray)


def process_hybrid(image_bgr, size, accelerator):
    """Resize in PL prin DMA, apoi grayscale si Sobel pe ARM."""
    small = accelerator.resize(image_bgr, size)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    return sobel_software(gray)


def locate_resizer():
    """Cauta doar perechi bit/hwh corecte, fara descarcari implicite."""
    candidates = [
        LAB_DIR / "overlay" / "resizer.bit",
        LAB_DIR.parent / "Lab5" / "overlay" / "resizer.bit",
    ]
    try:
        import pynq_helloworld
        candidates.append(
            Path(pynq_helloworld.__file__).resolve().parent /
            "notebooks" / "edge" / "resizer.bit"
        )
    except ImportError:
        pass
    for bit in candidates:
        if bit.is_file() and bit.with_suffix(".hwh").is_file():
            return bit
    raise FileNotFoundError(
        "Nu am gasit resizer.bit + resizer.hwh. "
        "Utilizati perechea functionala din Lab5/overlay/ "
        "sau pachetul pynq_helloworld."
    )


class ResizerHW:
    """Resize IP + AXI DMA din Lab5; fara Sobel accelerat."""

    def __init__(self, bitfile=None):
        from pynq import Overlay, allocate
        self._allocate = allocate
        self.bitfile = Path(bitfile) if bitfile else locate_resizer()
        if not self.bitfile.with_suffix(".hwh").exists():
            raise FileNotFoundError("Lipseste .hwh pentru " + str(self.bitfile))
        self.overlay = Overlay(str(self.bitfile))
        self.dma = self.overlay.axi_dma_0
        self.accel = self.overlay.resize_accel_0
        self._geometry = None
        self._input = None
        self._output = None

    def _configure(self, source_shape, target_size):
        height, width, channels = source_shape
        dst_width, dst_height = target_size
        if channels != 3:
            raise ValueError("Acceleratorul din Lab5 asteapta BGR pe 3 canale.")
        if not (height > 0 and width > 0 and dst_height > 0 and dst_width > 0):
            raise ValueError("Dimensiunile imaginii trebuie sa fie pozitive.")
        geometry = (height, width, dst_height, dst_width)
        if geometry == self._geometry:
            return
        self.close_buffers()
        self._input = self._allocate(shape=(height, width, 3), dtype=np.uint8)
        self._output = self._allocate(
            shape=(dst_height, dst_width, 3), dtype=np.uint8)
        regs = self.accel.register_map
        regs.src_rows = height
        regs.src_cols = width
        regs.dst_rows = dst_height
        regs.dst_cols = dst_width
        self._geometry = geometry

    @staticmethod
    def _wait_until_idle(channel, label, timeout_s=5.0):
        """Asteapta finalizarea transferului DMA, dar nu la infinit."""
        start = perf_counter()
        while not channel.idle:
            if channel.error:
                raise RuntimeError(
                    "Canalul DMA {} semnaleaza o eroare. "
                    "Verificati transferul si reporniti kernelul.".format(label)
                )
            if perf_counter() - start >= timeout_s:
                raise TimeoutError(
                    "DMA {} nu a devenit IDLE in {:.1f} s. "
                    "Intrerupeti executia si reporniti kernelul Jupyter "
                    "inainte de o noua incercare; verificati rezolutia, "
                    "lungimea transferului si TLAST.".format(label, timeout_s)
                )
            sleep(0.001)
        # Apelul este sigur acum: transferul s-a terminat.
        # Lasam driverul PYNQ sa faca invalidarea si contabilizarea.
        channel.wait()

    def resize(self, frame, target_size):
        if frame.dtype != np.uint8 or frame.ndim != 3:
            raise TypeError("Imaginea trebuie sa fie BGR uint8 cu 3 canale.")
        self._configure(frame.shape, target_size)
        np.copyto(self._input, frame)
        if hasattr(self._input, "flush"):
            self._input.flush()
        self.dma.sendchannel.transfer(self._input)
        self.dma.recvchannel.transfer(self._output)
        self.accel.write(0x00, 0x81)
        # Evitam asteptarea nelimitata din DMA.wait() daca un transfer se blocheaza.
        # Timpul de expirare este o protectie didactica, nu o masurare a latentei.
        self._wait_until_idle(self.dma.sendchannel, "MM2S")
        self._wait_until_idle(self.dma.recvchannel, "S2MM")
        if hasattr(self._output, "invalidate"):
            self._output.invalidate()
        return np.array(self._output, copy=True)

    def close_buffers(self):
        for name in ("_input", "_output"):
            buffer = getattr(self, name)
            if buffer is not None:
                buffer.freebuffer()
                setattr(self, name, None)
        self._geometry = None

    def close(self):
        self.close_buffers()


def measure_callable(fn, repeats=25, warmup=2):
    """Masoara apeluri complete, in milisecunde, nu doar nucleul PL."""
    for _ in range(warmup):
        fn()
    times = []
    for _ in range(repeats):
        t0 = perf_counter()
        fn()
        times.append((perf_counter() - t0) * 1000)
    return {"mean_ms": float(np.mean(times)),
            "median_ms": float(np.median(times)),
            "p95_ms": float(np.percentile(times, 95)),
            "fps_processing": float(1000.0 / np.mean(times))}


def compare_images(reference, candidate):
    if reference.shape != candidate.shape:
        raise ValueError("Formele imaginilor trebuie sa coincida.")
    diff = np.abs(reference.astype(np.int16) - candidate.astype(np.int16))
    return {"mae": float(np.mean(diff)),
            "max_abs": int(np.max(diff)),
            "fraction_nonzero": float(np.mean(diff != 0))}
