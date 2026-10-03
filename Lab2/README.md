# Lab2 — PS–PL, AXI GPIO și MMIO

Acest laborator continuă după familiarizarea cu PYNQ din Lab1 și analizează mai profund modul în care software-ul executat în **Processing System (PS)** controlează perifericele implementate în **Programmable Logic (PL)**.

Fluxul urmărit este:

```text
Python
  ↓
PYNQ API / AxiGPIO / MMIO
  ↓
AXI-Lite
  ↓
registre hardware
  ↓
Programmable Logic
```

## Cerințe

- PYNQ-Z2
- Base Overlay disponibil ca `base.bit`
- Lab1 parcurs
- fără componente externe

Notebook-urile folosesc informațiile din `ip_dict` pentru a identifica IP-urile și adresele hardware. Nu se presupun adrese fizice hard-codate.

## Taskuri Lab2

| Notebook | Activitate principală |
|---|---|
| [Lab2.1.ipynb](./Lab2.1.ipynb) | Explorarea Overlay-ului și a `ip_dict` |
| [Lab2.2.ipynb](./Lab2.2.ipynb) | Acces la AXI GPIO prin driverul PYNQ |
| [Lab2.3.ipynb](./Lab2.3.ipynb) | Acces direct la registre cu MMIO |
| [Lab2.4.ipynb](./Lab2.4.ipynb) | Comparație API PYNQ vs AxiGPIO vs MMIO |

## Rezultatul laboratorului

La final, studentul trebuie să poată explica traseul:

```text
Python → adresă fizică → AXI-Lite → registru IP → hardware în PL
```

și să distingă clar între un API software de nivel înalt și accesul direct la registrele unui periferic hardware.
