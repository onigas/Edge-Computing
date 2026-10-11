# Lab5 — Accelerarea hardware a procesării de imagine

În Lab4 am stabilit un baseline software pe procesorul ARM. În Lab5 executăm operația **Resize** într-un accelerator implementat în **Programmable Logic (PL)** și comparăm performanța cu OpenCV.

Fluxul principal este:

```text
DDR
 ↓
AXI DMA MM2S
 ↓
AXI4-Stream
 ↓
Resize accelerator
 ↓
AXI4-Stream
 ↓
AXI DMA S2MM
 ↓
DDR
```

Configurarea acceleratorului se face prin AXI-Lite.

## Accelerator

Lab5 utilizează acceleratorul Resize pentru PYNQ-Z2 din repository-ul `onigas/PYNQ-HelloWorld`.

Implementarea hardware utilizează interpolare **biliniară**.

Notebook-urile caută mai întâi fișierele `resizer.bit` și `resizer.hwh` local sau într-o instalare `pynq_helloworld`. Dacă nu sunt disponibile, încearcă descărcarea fișierelor oficiale pentru PYNQ-Z2.

Pentru utilizare offline, fișierele pot fi copiate manual în:

```text
Lab5/overlay/
├── resizer.bit
└── resizer.hwh
```

## Taskuri Lab5

| Notebook | Activitate principală |
|---|---|
| [Lab5.1.ipynb](./Lab5.1.ipynb) | Arhitectura acceleratorului și inspectarea Overlay-ului |
| [Lab5.2.ipynb](./Lab5.2.ipynb) | Primul resize executat în PL |
| [Lab5.3.ipynb](./Lab5.3.ipynb) | Comparația rezultatului CPU vs PL |
| [Lab5.4.ipynb](./Lab5.4.ipynb) | Descompunerea timpului: copie, DMA și accelerator |
| [Lab5.5.ipynb](./Lab5.5.ipynb) | Benchmark CPU vs FPGA și calculul speed-up-ului |

Sobel și pipeline-ul hardware Resize → Sobel vor fi introduse în **Lab6**.
