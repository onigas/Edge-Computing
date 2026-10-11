# Lab6.2 — Hardware implementation specification (PYNQ-Z2)

**Status: design specification, not a validated bitstream.**

This document is the engineering companion to Lab6.2.ipynb. The current
Lab5 resizer overlay is verified for Resize, but it **cannot** be loaded
as a fused Resize→Sobel overlay. Do not distribute speculative bit/hwh
files to students.

## Required architecture

```text
     Zynq PS (Python / PYNQ, DDR)
              |
         AXI4-MM (HP)
              |
         AXI DMA MM2S
              |
          AXI4-Stream
              |
       Resize (HLS IP)
              |
       Pixel format check
              |
       RGB/BGR to Grayscale
              |
       Sobel 3x3 with line buffers
              |
          AXI4-Stream
              |
          AXI DMA S2MM
              |
         AXI4-MM (HP)
              |
       DDR output (uint8)
```

AXI-Lite carries *control* (image dimensions, start, status).
AXI4-Stream carries *pixels*. AXI4-MM/HP connects DMA to DDR.
An AXI clock and reset domain should be verified end-to-end.

## Prerequisite: inspect the proven Resize IP

Before modifying its design, examine the actual Lab5 resizer HWH and
its top-level HDL/HLS signature:

1. Input and output stream data widths and packing
2. Control register map and src/dst dimensions
3. TLAST/TUSER/TKEEP semantics
4. Pixels or bytes per AXI beat and DMA transfer lengths
5. Pixel ordering (BGR vs RGB) and image alignment
6. Whether the IP supports AXI4-Stream backpressure correctly

**Never assume:** 24-bit BGR input implies 24-bit AXI TDATA, or that
TLAST always denotes the last pixel of a frame. AXI4-Stream Video
usually uses TLAST at line end, while DMA simple mode deals in
packets; any required bridging must be designed.

## Sobel kernel reference specification

For **numerical comparability** with Lab4/Lab6:

- Convert the resized 3-channel image to uint8 grayscale.
- Apply 3x3 Sobel coefficients for Gx and Gy.
- Define and document **boundary handling** explicitly.
- Magnitude = sqrt(Gx^2 + Gy^2), saturate and round to uint8.

The notebook's 3-line model uses BORDER_CONSTANT; the standard
Lab4 software helper uses OpenCV's default border unless explicitly
overridden. The hardware reference must use the SAME boundary policy.

Possible hardware optimizations (L1 magnitude |Gx|+|Gy|, shift-based
approximations, thresholded edges) **change the numerical algorithm**.
Report numerical errors and do not call them an identical operation.

A Sobel 3x3 streaming core requires a neighborhood window and one/two
stored prior scan lines depending on the chosen line-buffer
architecture. BRAM estimates depend on pixel width and maximum image
width, not on complete frame height.

## Vivado / Vitis 2022.2 implementation checklist

1. Reuse or rebuild the *working* 2022.2-compatible Resize HLS IP.
2. Define a grayscale and Sobel hardware function with explicit
   AXI4-Stream types and line buffering (RTL or Vitis HLS).
3. Write **unit testbenches** for 1x1, 3x3, maximum-size and border
   frames; check no data loss under backpressure.
4. Construct the Vivado block design with AXI DMA, suitable memory
   interconnect, AXI-Lite control, clock/reset and stream conversion.
5. Validate packet boundaries, TLAST/TUSER, TKEEP and output DMA byte
   count. Incorrect framing can cause DMA wait() to hang.
6. Run synthesis and implementation; check utilization and timing
   closure (LUT/FF/BRAM/DSP, achievable clock).
7. Export both matching artifacts to Lab6/overlay:
   **resize_sobel.bit** and **resize_sobel.hwh**.
8. Inspect the overlay from PYNQ: list DMA/IP and addresses from
   overlay.ip_dict, without hard-coded physical addresses.
9. Verify an image and numerical error **before** benchmarking.
10. Measure kernel+DMA, full processing path, then video end-to-end FPS.

**Acceptance criteria:** reproducible processing of 30 consecutive
frames without stalled DMA, correct output geometry, quantified
numerical error, and a timing table clearly separating acquisition,
transfer and processing.

## Hardware experiments once the overlay exists

| Configuration | Intermediate DDR? | Output |
| --- | --- | --- |
| ARM OpenCV Resize→Sobel | Software-owned arrays | Grayscale Sobel |
| Hybrid PL Resize + ARM Sobel | **Yes** (return to ARM) | Grayscale Sobel |
| Sequential PL Resize then PL Sobel | **Yes** (DMA write/read) | Grayscale Sobel |
| Fused PL Resize→Sobel | **No full-frame intermediate** | Grayscale Sobel |

The last two rows require dedicated or reconfigurable hardware; they
cannot be inferred from measurements using the Lab5 resizer alone.
DDR payload savings in Lab6.2 are **analytical estimates**, not
external-memory-controller measurements.

## Reference designs

- PYNQ-HelloWorld: https://github.com/Xilinx/PYNQ-HelloWorld
- PYNQ Composable Pipeline:
  https://github.com/Xilinx/PYNQ_Composable_Pipeline

The composable overlay provides other stream-connected vision blocks
and can be studied as an alternative demonstration. It does **not**
supply this exact Resize→Sobel bitstream ready for the present lab.
