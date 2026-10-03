# Lab3 — Buffere, AXI4-Stream și DMA

Acest laborator introduce transferul eficient al datelor între **Processing System (PS)** și **Programmable Logic (PL)**.

În Lab2 am controlat periferice prin registre AXI-Lite. Pentru volume mari de date — vectori, imagini și cadre video — vom utiliza **AXI4-Stream** și **DMA**.

Fluxul de bază este:

```text
DDR / PS
   ↓
DMA
   ↓
AXI4-Stream
   ↓
hardware în PL
   ↓
AXI4-Stream
   ↓
DMA
   ↓
DDR / PS
```

## Cerințe

- PYNQ-Z2
- Lab1 și Lab2 parcurse
- Python / NumPy / PYNQ
- acces la fișierele `dma_tutorial.bit` și `dma_tutorial.hwh`

## Overlay DMA

Lab3 reutilizează designul verificat din:

```text
onigas/PYNQ_Workshop
└── Session_4/
    └── bitstream/
        ├── dma_tutorial.bit
        └── dma_tutorial.hwh
```

Notebook-urile Lab3.2–Lab3.5 verifică automat directorul local `bitstream/`. Dacă fișierele lipsesc și placa are acces la Internet, ele sunt descărcate automat din repository-ul `PYNQ_Workshop`.

Pentru utilizare fără Internet, copiați manual cele două fișiere în:

```text
Lab3/bitstream/
```

## Taskuri Lab3

| Notebook | Activitate principală |
|---|---|
| [Lab3.1.ipynb](./Lab3.1.ipynb) | `pynq.allocate()` și buffere pentru PS–PL |
| [Lab3.2.ipynb](./Lab3.2.ipynb) | AXI4-Stream și pregătirea Overlay-ului DMA |
| [Lab3.3.ipynb](./Lab3.3.ipynb) | DMA loopback: PS → PL → PS |
| [Lab3.4.ipynb](./Lab3.4.ipynb) | Transferuri cu dimensiuni diferite |
| [Lab3.5.ipynb](./Lab3.5.ipynb) | Benchmark: latență și throughput |

## Rezultatul laboratorului

La final, studentul trebuie să poată explica și măsura traseul:

```text
buffer DDR → DMA send → AXI4-Stream → PL → DMA receive → buffer DDR
```

și să distingă între:

- dimensiunea payload-ului;
- latența end-to-end;
- throughput-ul efectiv;
- overhead-ul fix al transferului.
