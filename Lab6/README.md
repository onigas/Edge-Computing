# Lab6 — Video Processing Pipelines and Edge Performance

**Platform:** PYNQ-Z2, PYNQ 2.7.0; Python/Jupyter, OpenCV and the proven
PYNQ-HelloWorld Resize overlay from Lab5.

## Goal

Understand why a **fused AXI4-Stream hardware pipeline** differs from two
sequential hardware kernels, and how data transfers and video acquisition
change application-level FPS.

This lab uses **three substantial notebooks**, not independent miniature
exercises:

| Notebook | What students build or evaluate | Execution status |
| --- | --- | --- |
| [Lab6.1](Lab6.1.ipynb) | ARM Resize+Sobel vs FPGA Resize + ARM Sobel (same image/geometry, correctness and timing) | Executable with working Lab5 Resize overlay |
| [Lab6.2](Lab6.2.ipynb) | Three-row streaming Sobel reference, AXI4-Stream handshake, sequential-vs-fused DDR traffic model; target hardware design | Executable **software model**; no fused PL overlay is claimed |
| [Lab6.3](Lab6.3.ipynb) | Video (synthetic, file or USB camera), same CPU/hybrid pathways, measured acquisition and end-to-end timing | Executable with same Lab5 overlay for hybrid path |

## Lab6.2 target architecture (not yet available as a verified overlay)

```text
DDR source frame (BGR)
         |
    AXI DMA MM2S
         |
     Resize RGB
         |
   RGB to grayscale
         |
    Sobel 3x3 (line buffers)
         |
    AXI DMA S2MM
         |
DDR result (grayscale)
```

The data between PL blocks must move through **AXI4-Stream** without an
intermediate full-frame write/read in DDR. A real hardware experiment requires
a new PYNQ-Z2 bitstream **and matching .hwh**, with the appropriate DMA,
AXI-Lite controls, stream widths, framing/TLAST and backpressure validated.
**The existing resizer.bit is not such an overlay.**

Notebook 6.2 distinguishes carefully between:
- **software functional model:** line buffers and Sobel results on ARM;
- **analytical model:** minimum DDR payload bytes, without bus/protocol overhead;
- **hardware implementation:** future PL synthesis/bitstream validation.

Do not interpret analytical throughput or Python simulation as measured
FPGA throughput.

## Setup on the PYNQ-Z2

1. Clone/copy the **entire** repository; notebooks require
   ../Lab4/images/fruits.jpg.
2. Complete Lab5. The same working resizer.bit + resizer.hwh files are
   searched in ../Lab5/overlay/ or in the installed pynq_helloworld package.
   You can alternatively copy the pair to Lab6/overlay/.
3. Open a Jupyter terminal, enter the cloned repository, then open
   Lab6/Lab6.1.ipynb and run top-to-bottom.
4. Continue with Lab6.2 and Lab6.3. In Lab6.3 select a synthetic source
   (no camera required), local video file, or USB camera.
5. Do not run two notebooks controlling different overlays at the same time.

For the detailed Vivado/Vitis hardware implementation and validation plan, see
[Lab6.2 hardware specification](hardware/README.md).

## Learning outcomes

- Connect functional correctness with numerical error metrics and pipeline
  architecture.
- Distinguish **AXI4-Stream** handshake from whole-frame transfer through
  **AXI DMA and DDR**.
- Quantify the theoretical DDR traffic eliminated by stream fusion.
- Understand line buffering, boundary conditions and streaming latency.
- Benchmark processing latency separately from frame acquisition and
  application end-to-end time, recording mean/p95/FPS.
- Identify when the camera/source rather than the PL kernel is the bottleneck.

## Submission

**One technical report** integrating all three notebooks:
architecture diagram, image validation, performance tables, assumptions
behind DDR estimates, and a reasoned conclusion about edge-computing
viability. The report must state clearly which results were **measured on
hardware** and which are **models/estimates**.

## Hardware references

- PYNQ-HelloWorld Resize (compatible PYNQ 2.7):
  https://github.com/Xilinx/PYNQ-HelloWorld
- PYNQ Composable Pipeline (PYNQ-Z2 and ready-made stream composition;
  optional inspiration, not an interchangeable Resize→Sobel bitstream):
  https://github.com/Xilinx/PYNQ_Composable_Pipeline
