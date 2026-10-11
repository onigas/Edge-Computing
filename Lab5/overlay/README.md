# Resize Overlay

Pentru utilizare offline sunt necesare:

```text
resizer.bit
resizer.hwh
```

Sursa: `onigas/PYNQ-HelloWorld`, exemplul Resize pentru PYNQ-Z2.

Designul conține un AXI DMA, interfață AXI4-Stream, acceleratorul HLS `resize_accel`, registre AXI-Lite și acces la DDR prin portul HP al Zynq.

Acceleratorul folosește interpolare biliniară.
