# Lab4 — Prelucrare de imagine în software pe ARM

Lab4 stabilește **baseline-ul software** pentru operațiile de imagine care vor fi accelerate în Lab5.

Toate operațiile din acest laborator rulează pe **Processing System (ARM Cortex-A9)**. Nu este utilizat un accelerator FPGA.

Fluxul de lucru este:

```text
Imagine
   ↓
NumPy / OpenCV
   ↓
ARM Cortex-A9
   ↓
grayscale / resize / Sobel
   ↓
timp de execuție / FPS
```

## Cerințe

- PYNQ-Z2
- Python
- NumPy
- OpenCV (`cv2`)
- Matplotlib
- fără hardware extern

## Imagine de test

Notebook-urile utilizează imaginea `opencv_filters.jpg` existentă în repository-ul `onigas/PYNQ`.

Dacă imaginea nu există local, notebook-ul încearcă să o descarce automat. Pentru utilizare offline, copiați imaginea în:

```text
Lab4/images/opencv_filters.jpg
```

## Taskuri Lab4

| Notebook | Activitate principală |
|---|---|
| [Lab4.1.ipynb](./Lab4.1.ipynb) | Reprezentarea imaginilor cu NumPy și OpenCV |
| [Lab4.2.ipynb](./Lab4.2.ipynb) | Conversie color → grayscale |
| [Lab4.3.ipynb](./Lab4.3.ipynb) | Resize în software |
| [Lab4.4.ipynb](./Lab4.4.ipynb) | Detecția muchiilor cu Sobel |
| [Lab4.5.ipynb](./Lab4.5.ipynb) | Benchmark software: timp, FPS și rezoluție |

## Rezultatul laboratorului

La finalul Lab4 se obține un baseline măsurabil:

```text
T_grayscale
T_resize
T_sobel
T_pipeline
FPS_software
```

Aceste valori vor fi utilizate în Lab5 pentru comparația cu acceleratorul hardware:

```text
speed-up = T_software / T_hardware
```
