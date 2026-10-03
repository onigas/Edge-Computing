# Edge Computing cu PYNQ-Z2

Acest repository conține lucrările practice pentru un set de laboratoare de nivel **master** dedicate arhitecturilor **Edge Computing** bazate pe platforma **PYNQ-Z2 / Xilinx Zynq-7000**.

Obiectivul principal este parcurgerea progresivă a traseului:

```text
Python / Jupyter
      ↓
Processing System (PS)
      ↓
AXI / MMIO / DMA
      ↓
Programmable Logic (PL)
      ↓
Accelerare hardware
      ↓
Prelucrare de imagine
      ↓
Inferență AI accelerată
```

Laboratoarele urmăresc nu doar funcționarea aplicațiilor, ci și înțelegerea relației dintre software și hardware, precum și evaluarea performanței sistemelor Edge prin măsurarea latenței, throughput-ului și a costului transferurilor PS–PL.

---

## Platformă

Laboratoarele sunt dezvoltate pentru:

- **PYNQ-Z2**
- SoC **Xilinx Zynq-7000**
- procesor ARM Cortex-A9 în **Processing System (PS)**
- logică FPGA în **Programmable Logic (PL)**
- Linux + Python + Jupyter
- PYNQ 3.x

Pentru primele laboratoare nu sunt necesare componente externe. Sunt utilizate resursele integrate pe placă: LED-uri, switch-uri și butoane.

---

## Structura repository-ului

Fiecare laborator este organizat într-un director propriu:

```text
Edge-Computing/
├── Lab1/
│   ├── README.md
│   ├── Lab1.1.ipynb
│   ├── Lab1.2.ipynb
│   ├── Lab1.3.ipynb
│   ├── Lab1.4.ipynb
│   └── Lab1.5.ipynb
└── ...
```

Fișierul `README.md` din fiecare laborator conține informațiile generale, cerințele de conectare și indicațiile necesare înainte de rularea notebook-urilor.

Notebook-urile trebuie parcurse în ordine.

---

## Laboratoare

### Lab1 — Introducere în PYNQ și control GPIO

[Deschide Lab1](./Lab1/README.md)

| Notebook | Activitate principală |
|---|---|
| [Lab1.1.ipynb](./Lab1/Lab1.1.ipynb) | Verificarea mediului PYNQ |
| [Lab1.2.ipynb](./Lab1/Lab1.2.ipynb) | Încărcarea Base Overlay și controlul LED-urilor |
| [Lab1.3.ipynb](./Lab1/Lab1.3.ipynb) | Citirea switch-urilor și controlul LED-urilor |
| [Lab1.4.ipynb](./Lab1/Lab1.4.ipynb) | Citirea butoanelor |
| [Lab1.5.ipynb](./Lab1/Lab1.5.ipynb) | Contor binar pe 4 biți controlat cu butoane |

---

## Direcția următoare a laboratoarelor

Seria de laboratoare va continua gradual cu:

1. explorarea Overlay-urilor și a arhitecturii PS–PL;
2. acces la periferice prin **AXI GPIO** și **MMIO**;
3. buffere partajate și transferuri de date prin **AXI DMA**;
4. prelucrare de imagine în software;
5. accelerarea hardware a operațiilor de imagine;
6. pipeline-uri de procesare în PL;
7. evaluarea latenței și throughput-ului pentru aplicații Edge;
8. rețele neuronale cuantizate și accelerarea inferenței;
9. aplicații Edge AI pe PYNQ-Z2.

---

## Mod de lucru

1. Se pornește placa PYNQ-Z2 și se realizează conexiunea la rețea.
2. Se accesează interfața Jupyter din browser.
3. Se deschide directorul laboratorului curent.
4. Se citesc mai întâi instrucțiunile din `README.md`.
5. Notebook-urile se execută în ordine numerică.
6. Codul se modifică și se testează direct pe placă.

Pentru detalii privind conectarea și depanarea rețelei, consultați:

[Lab1 — Conectarea la placa PYNQ-Z2](./Lab1/README.md)

---

## Observație

Codul Python rulează pe procesorul ARM din **Processing System**. Logica FPGA din **Programmable Logic** nu execută direct Python; ea este configurată și controlată din software prin infrastructura PYNQ și interfețele AXI.

Această separare PS–PL constituie baza laboratoarelor ulterioare de accelerare hardware pentru Edge Computing.
