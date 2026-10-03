# Edge Computing cu PYNQ-Z2 și Kria Robotics

Acest repository conține lucrările practice pentru un curs de nivel **master** dedicat sistemelor **Edge Computing** bazate pe platforme AMD/Xilinx SoC și FPGA.

Prima parte a cursului utilizează **PYNQ-Z2 / Zynq-7000** pentru înțelegerea relației dintre software și hardware, a comunicației PS–PL, a transferurilor de date și a accelerării hardware.

După cele șapte laboratoare PYNQ-Z2, cursul continuă pe platforma **Kria Robotics**, unde accentul se mută către sisteme robotice, ROS 2, percepție și aplicații Edge AI integrate.

---

## Obiectiv general

Traseul urmărit este:

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
      ↓
Kria Robotics + ROS 2
      ↓
Proiect robotic integrat
```

Laboratoarele urmăresc nu doar funcționarea aplicațiilor, ci și înțelegerea arhitecturii și evaluarea performanței prin măsurarea latenței, throughput-ului și a costului transferurilor PS–PL.

---

# Etapa I — PYNQ-Z2

## Platformă

Laboratoarele sunt dezvoltate pentru:

- **PYNQ-Z2**
- SoC **Xilinx Zynq-7000**
- ARM Cortex-A9 în **Processing System (PS)**
- logică FPGA în **Programmable Logic (PL)**
- Linux + Python + Jupyter
- PYNQ 3.x

Pentru primele laboratoare nu sunt necesare componente externe.

---

## Structura celor 7 laboratoare PYNQ-Z2

| Laborator | Tema principală |
|---|---|
| **Lab1** | Introducere în PYNQ, Base Overlay și GPIO |
| **Lab2** | Overlay, AXI GPIO, AXI-Lite și MMIO |
| **Lab3** | Buffere, memorie partajată și AXI DMA |
| **Lab4** | Prelucrare de imagine în software pe ARM |
| **Lab5** | Accelerarea hardware a procesării de imagine |
| **Lab6** | Pipeline streaming și procesare video Edge |
| **Lab7** | Inferență AI accelerată și rețele cuantizate |

---

## Lab1 — Introducere în PYNQ și control GPIO

[Deschide Lab1](./Lab1/README.md)

| Notebook | Activitate principală |
|---|---|
| [Lab1.1.ipynb](./Lab1/Lab1.1.ipynb) | Verificarea mediului PYNQ |
| [Lab1.2.ipynb](./Lab1/Lab1.2.ipynb) | Încărcarea Base Overlay și controlul LED-urilor |
| [Lab1.3.ipynb](./Lab1/Lab1.3.ipynb) | Citirea switch-urilor și controlul LED-urilor |
| [Lab1.4.ipynb](./Lab1/Lab1.4.ipynb) | Citirea butoanelor |
| [Lab1.5.ipynb](./Lab1/Lab1.5.ipynb) | Contor binar pe 4 biți controlat cu butoane |

---

## Lab2 — PS–PL, AXI și MMIO

[Deschide Lab2](./Lab2/README.md)

| Notebook | Activitate principală |
|---|---|
| [Lab2.1.ipynb](./Lab2/Lab2.1.ipynb) | Explorarea Overlay-ului și a `ip_dict` |
| [Lab2.2.ipynb](./Lab2/Lab2.2.ipynb) | Acces la AXI GPIO prin driverul PYNQ |
| [Lab2.3.ipynb](./Lab2/Lab2.3.ipynb) | Acces direct la registre cu MMIO |
| [Lab2.4.ipynb](./Lab2/Lab2.4.ipynb) | Comparație API PYNQ vs AxiGPIO vs MMIO |

---

## Lab3 — Buffere și AXI DMA

Direcția laboratorului:

- `pynq.allocate()`;
- buffere accesibile PS și PL;
- AXI4-Stream;
- transfer PS → PL → PS;
- DMA loopback;
- măsurarea latenței și throughput-ului.

---

## Lab4 — Prelucrare de imagine în software

Direcția laboratorului:

- reprezentarea imaginilor în memorie;
- NumPy / OpenCV;
- grayscale;
- resize;
- filtre și Sobel;
- măsurarea timpului de execuție și FPS;
- stabilirea unui baseline software pentru comparația cu FPGA.

---

## Lab5 — Accelerarea hardware a procesării de imagine

Direcția laboratorului:

- încărcarea unui Overlay cu accelerator;
- transferul imaginilor prin DMA;
- resize și/sau Sobel în PL;
- măsurarea timpului de execuție;
- comparație CPU vs FPGA;
- calculul speed-up-ului.

---

## Lab6 — Pipeline streaming și procesare video Edge

Direcția laboratorului:

- procesare în flux;
- pipeline-uri hardware;
- Resize → Sobel;
- reducerea acceselor intermediare la DDR;
- procesare video;
- latență end-to-end;
- throughput și FPS.

---

## Lab7 — Inferență AI accelerată

Direcția laboratorului:

- cuantizarea rețelelor neuronale;
- BNN/QNN;
- inferență pe ARM;
- inferență accelerată în PL;
- comparația preciziei, latenței și throughput-ului;
- introducere în Edge AI.

---

# Etapa II — Kria Robotics

După finalizarea celor șapte laboratoare PYNQ-Z2, cursul continuă pe platforma **Kria Robotics**.

Primele laboratoare Kria vor introduce:

- arhitectura Kria SOM;
- Linux pe Kria;
- ROS 2;
- noduri, topicuri, publishers și subscribers;
- achiziție de date de la senzori;
- camere și procesare de imagine;
- percepție accelerată;
- integrarea acceleratoarelor hardware într-un sistem robotic.

După această etapă introductivă, activitatea va continua sub forma unui **proiect integrator**.

---

## Direcția proiectului

Proiectul va combina:

```text
Senzori / Cameră / LiDAR
          ↓
      Percepție
          ↓
  Procesare / Edge AI
          ↓
       ROS 2
          ↓
      Decizie
          ↓
 Control robotic
```

O direcție posibilă este dezvoltarea unui **robot mobil autonom pentru medii indoor**, cum ar fi o magazie, un spital sau un laborator.

Obiectivul proiectului este integrarea într-un singur sistem a conceptelor studiate anterior:

- achiziție senzorială;
- procesare în timp real;
- accelerare hardware;
- inferență AI;
- ROS 2;
- control și decizie robotică.

---

## Mod de lucru

1. Se citește fișierul `README.md` al laboratorului.
2. Notebook-urile se execută în ordine numerică.
3. Codul se rulează și se modifică direct pe platforma hardware.
4. Rezultatele se verifică experimental.
5. În laboratoarele de performanță se măsoară explicit latența, throughput-ul și speed-up-ul.

Pentru conectarea și depanarea PYNQ-Z2 consultați:

[Lab1 — Conectarea la placa PYNQ-Z2](./Lab1/README.md)

---

## Observație arhitecturală

Codul Python rulează pe procesorul ARM din **Processing System**. Logica FPGA din **Programmable Logic** nu execută direct Python; ea este configurată și controlată din software prin infrastructura PYNQ și interfețele AXI.

Această separare PS–PL constituie baza pentru laboratoarele de accelerare hardware și pentru tranziția ulterioară către aplicații Edge AI și robotică pe Kria.
