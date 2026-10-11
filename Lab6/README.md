# Lab6 — Pipeline streaming și procesare video Edge

**Platformă:** PYNQ-Z2, PYNQ 2.7.0, Python/Jupyter, OpenCV și acceleratorul Resize folosit în Lab5.

## Obiectiv

Studiem de ce un **pipeline hardware conectat direct prin AXI4-Stream** este diferit de executarea secvențială a unor acceleratoare cu rezultate intermediare în DDR. Evaluăm și influența achiziției video și a transferurilor asupra latenței totale și FPS-ului aplicației.

Laboratorul conține **trei notebook-uri ample și corelate**:

| Notebook | Activitate | Stadiu |
| --- | --- | --- |
| [Lab6.1](Lab6.1.ipynb) | Resize + Sobel integral pe ARM versus Resize în FPGA + Sobel pe ARM; verificarea rezultatului și benchmark | Executabil cu overlay-ul Resize funcțional din Lab5 |
| [Lab6.2](Lab6.2.ipynb) | Sobel cu trei linii, AXI4-Stream, TVALID/TREADY, comparație de trafic DDR și arhitectura pipeline-ului | Model software și analiză arhitecturală; **nu** este un overlay PL complet |
| [Lab6.3](Lab6.3.ipynb) | Sursă sintetică, fișier video sau cameră USB; latență de achiziție, procesare, end-to-end și FPS | Executabil cu overlay-ul Resize funcțional din Lab5 pentru calea hibridă |

## Arhitectura hardware-țintă

```text
Imagine BGR în DDR
       |
 AXI DMA MM2S
       |
 Resize (PL)
       |
 BGR → grayscale (PL)
       |
 Sobel 3×3 (PL, buffere de linii)
       |
 AXI DMA S2MM
       |
Rezultat grayscale în DDR
```

Blocurile din PL trebuie conectate direct prin **AXI4-Stream**, fără scrierea imaginii intermediare în DDR. Această arhitectură necesită o **nouă pereche bit/hwh validată**. Overlay-ul `resizer.bit` utilizat în Lab5 nu implementează și Sobel în PL.

În Lab6.2 distingem riguros:
- **model funcțional software:** prelucrare Sobel cu buffere de linii în Python;
- **model analitic:** volum minim de date transferate din/în DDR;
- **implementare hardware:** proiectare și validare într-un viitor overlay PYNQ-Z2.

**Nu prezentăm estimările de trafic sau simulările Python ca performanțe FPGA măsurate.**

## Instalare în configurația actuală a laboratorului

Pe placă există deja directorul `Lab2026`, copiat manual în Jupyter. **Nu este un repository Git clonat**, deci nu se folosește `git pull`.

Deschideți un terminal Jupyter și executați:

```bash
cd /home/xilinx/jupyter_notebooks/Lab2026
curl -L https://github.com/onigas/Edge-Computing/archive/refs/heads/main.tar.gz | tar -xz --strip-components=1 Edge-Computing-main/Lab6
```

Această comandă descarcă doar `Lab6` în `Lab2026/Lab6`, lângă directoarele Lab1–Lab5, și poate actualiza fișierele Lab6 existente.

**Prerechizite:**
1. Fișierul `../Lab4/images/fruits.jpg` trebuie să existe față de notebook-uri.
2. Pentru experimente FPGA, folosiți fișierele funcționale `resizer.bit` și `resizer.hwh` din `../Lab5/overlay/`. Pot fi folosite și cele din pachetul `pynq_helloworld` sau o pereche copiată în `Lab6/overlay/`.
3. Începeți cu `Lab6.1.ipynb`, continuați cu `Lab6.2.ipynb`, apoi `Lab6.3.ipynb`.
4. **La prima verificare hardware păstrați rezoluția 320 × 240.** Alte rezoluții se testează doar după confirmarea funcționării DMA.

## Dacă o celulă se blochează

- Folosiți **Kernel → Interrupt** pentru a întrerupe execuția.
- Codul comun conține o verificare a finalizării canalelor DMA, cu **timeout de 5 secunde** pentru fiecare canal, evitând un apel `wait()` fără limită de timp.
- Dacă apare `TimeoutError`, nu reporniți imediat aceeași celulă: **Kernel → Restart** și verificați configurația transferului (dimensiune, număr de octeți, `TLAST`).
- Nu porniți simultan notebook-uri care reprogramează FPGA-ul.

## Competențe urmărite

- Identificarea blocurilor AXI DMA, AXI-Lite, AXI4-Stream și a transferurilor prin DDR.
- Implementarea și verificarea unui model Sobel cu trei linii.
- Explicarea mecanismului `TVALID/TREADY` și a semnalelor de delimitare.
- Estimarea traficului DDR eliminat prin conectarea directă a acceleratoarelor.
- Măsurarea separată a procesării și a latenței complete a unei aplicații video.
- Interpretarea situațiilor în care avantajul acceleratorului este limitat de achiziția video.

## Livrabil

Un **raport tehnic comun** pentru cele trei notebook-uri: diagrame, validare numerică, măsurători de latență și FPS, ipoteze ale modelului DDR și concluzii. Rezultatele **măsurate** trebuie separate de estimări și simulări.

Pentru detalii despre implementarea reală în FPGA consultați [specificația hardware pentru Lab6.2](hardware/README.md).

## Referințe

- PYNQ-HelloWorld (accelerator Resize): https://github.com/Xilinx/PYNQ-HelloWorld
- PYNQ Composable Pipeline (exemple de conexiuni streaming, nu același overlay Resize → Sobel): https://github.com/Xilinx/PYNQ_Composable_Pipeline

**Test hardware real:** [Lab6.2_FPGA.ipynb](Lab6.2_FPGA.ipynb) — validează pe PYNQ-Z2 overlay-ul `resize_sobel.bit` / `resize_sobel.hwh` (test sintetic și benchmark). Acesta este un notebook suplimentar și nu înlocuiește Lab6.2.
