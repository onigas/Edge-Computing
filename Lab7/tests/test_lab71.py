"""Software-only tests; fake scores do not validate a neural model."""
import csv
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import lab71 as lab
import numpy as np
from PIL import Image

class Adapter:
    def image_to_cifar(self, image, stream):
        mode = getattr(Image, 'Resampling', Image)
        image.thumbnail((32, 32), mode.LANCZOS)
        bg = Image.new('RGBA', (32, 32), (255, 255, 255, 0))
        bg.paste(image, ((32-image.width)//2, (32-image.height)//2))
        a = np.array(bg)
        stream.write(bytes([1]))
        for c in range(3):
            stream.write(a[:, :, c].flatten().tobytes())

class Tests(unittest.TestCase):
    def test_hash(self):
        b = (lab.ROOT/'images/reference/deer.bin').read_bytes()
        self.assertEqual(lab.git_blob_sha(b), lab.REFERENCE_SHA)
        self.assertEqual(b[0], 1)
    def test_roundtrip(self):
        png = lab.prepare_reference()
        stream = io.BytesIO()
        Adapter().image_to_cifar(lab.read_rgb(png), stream)
        self.assertEqual(stream.getvalue(), png.with_suffix('.bin').read_bytes())
    def test_preserves_image(self):
        image = Image.new('RGB', (120, 70))
        self.assertEqual(lab.network_input(Adapter(), image).shape, (32, 32, 3))
        self.assertEqual(image.size, (120, 70))
    def test_bad_record(self):
        with self.assertRaises(ValueError): lab.decode_cifar_record(b'bad')
    def test_labels(self):
        labels = lab.load_labels(lab.ROOT/'images/labels.csv')
        self.assertEqual(lab.expected_label(lab.ROOT/'images/reference/deer.png', labels), 4)
        self.assertEqual(lab.expected_label(lab.ROOT/'images/own/Cat/x.png', {}), 3)
        self.assertIsNone(lab.expected_label(lab.ROOT/'images/own/Other/x.png', {}))
    def test_bad_labels(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'labels.csv'
            for text in ('file,class_id\nx,10\n', 'file,class_id\nx,2\nx,3\n'):
                p.write_text(text)
                with self.assertRaises(ValueError): lab.load_labels(p)
    def test_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/'out.csv'
            lab.save_csv(p, [{'file':'x'}, {'file':'y','error':'bad'}])
            with p.open() as f: rows = list(csv.DictReader(f))
            self.assertEqual(rows[1]['error'], 'bad')
    def test_archive(self):
        with tempfile.TemporaryDirectory() as tmp:
            def fake_download(url, target):
                with zipfile.ZipFile(str(target), 'w') as z:
                    for p in ('bnn/bnn.py','bnn/__init__.py','bnn/params/cifar10/cnvW2A2/x.bin','Lab1/x'):
                        z.writestr('snapshot/'+p, b'test')
            with mock.patch.object(lab, 'ROOT', Path(tmp)), mock.patch.object(lab, 'download_file', fake_download):
                out = lab._fetch_local_runtime()
                self.assertTrue((out/'bnn/bnn.py').is_file())
                self.assertFalse((out/'Lab1').exists())
                self.assertEqual(json.loads((out/'LAB71_SOURCE.json').read_text())['revision'], lab.REVISION)
    def test_board_guard(self):
        with mock.patch.dict(lab.os.environ, {'BOARD':'other'}):
            with self.assertRaises(RuntimeError): lab.load_bnn(False)
    def test_wrapper(self):
        class Fake:
            classes = lab.CLASS_NAMES
            usecPerImage = 123.0
            def classify_image_details(self, image): return np.arange(10, dtype=np.int32)
        with mock.patch.object(lab, 'check_overlay'):
            report, _, _ = lab.infer_file(Fake(), lab.prepare_reference())
        self.assertEqual(report['prediction_id'], 9)
        self.assertEqual(report['library_reported_ms'], 0.123)
        self.assertGreaterEqual(report['file_to_prediction_ms'], report['api_ms'])

if __name__ == '__main__': unittest.main()
