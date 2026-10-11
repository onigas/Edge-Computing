# Lab6.2 — Etapa HLS Resize (Vitis HLS 2022.2)

**Stadiu: surse și testbench pregătite; încă neverificate în Vitis HLS pe calculatorul laboratorului.**

Acest subproiect reconstruiește IP-ul de **Resize cu AXI4-Stream** din
[Xilinx/PYNQ-HelloWorld](https://github.com/Xilinx/PYNQ-HelloWorld),
folosind **Vitis Vision 2022.2** și placa **PYNQ-Z2 (xc7z020clg400-1)**.
Nu include încă nucleul Sobel și nu produce automat overlay-ul final al Lab6.2.

## Conținut

| Fișier | Rol |
| --- | --- |
| `xf_resize_accel_stream.cpp` | Sursă HLS pentru IP Resize |
| `resize_accel.hpp` | Tipul `ap_axiu<24,1,1,1>` și declarația funcției de top |
| `tb_resize.cpp` | Test automat pentru două dimensiuni, lungimea fluxului, culoare, `TKEEP` și `TLAST` |
| `build_resize.tcl` | Proiect Vitis HLS: `csim`, `csynth` sau `export` |

## Adaptări față de sursa originală

1. `xf::cv::ap_axiu<24,1,1,1>` → `ap_axiu<24,1,1,1>`, pentru tipurile HLS din Vitis 2022.2.
2. În `axis2xfMat` și `xfMat2axis`, indexarea liniară `i*rows+j` a fost schimbată în `i*cols+j` (lățimea, nu înălțimea, determină pasul dintre linii).
3. Sunt inițializate explicit câmpurile AXI laterale la ieșire (`TKEEP`, `TSTRB`, `TUSER`, `TID`, `TDEST`).
4. Se păstrează interfața de **24 biți**, interpolarea biliniară și
   **TLAST numai la ultimul pixel al cadrului** (convenția DMA folosită în Lab5).
5. Dimensiunile maxime statice rămân cele din sursa originală, **3840×2160**;
   aceste limite pot necesita optimizare după primul raport de sinteză.

Pentru Vitis Vision **2022.2**, apelul `xf::cv::resize<...>` cu
`MAXDOWNSCALE` drept al optulea parametru șablon este încă valid; nu utilizăm
semnăturile din ramuri Vitis Vision mai recente.

## Cea mai simplă variantă: lansare automată pe Windows

Din directorul `Lab6/hardware/resize_hls/` de pe **calculatorul cu Vitis HLS
2022.2 instalat**, executați prin dublu clic
[`START_CSIM_WINDOWS.bat`](START_CSIM_WINDOWS.bat).

Scriptul verifică disponibilitatea `vitis_hls`, încearcă să găsească
instalarea în căile Windows standard și, la nevoie, descarcă prin Git doar
fișierele necesare din Vitis Vision **2022.2**. Apoi rulează **C Simulation**
și salvează rezultatele în `resize_csim.log`.

**Nu execută automat sinteza sau exportul IP.** Dacă instalarea Vitis se află
într-o altă locație și nu este în PATH, scriptul solicită pornirea din
`Vitis HLS 2022.2 Command Prompt`. Un rezultat de tip `OK` la simulare
trebuie confirmat înainte de pasul următor.

---

## Pregătire pe PC-ul Windows cu Vitis HLS 2022.2

**Nu rulați scriptul pe PYNQ-Z2.** Sinteza HLS se execută pe calculatorul cu instrumentele AMD/Xilinx.

Pe PC, amplasați cele două repository-uri în directoare alăturate, de exemplu
`C:/FPGA/Edge-Computing` și `C:/FPGA/Vitis_Libraries`.

Obținerea bibliotecii necesare (din CMD sau Git Bash pe PC):

```bat
cd /d C:\FPGA
git clone --depth 1 --filter=blob:none --sparse --branch 2022.2 https://github.com/Xilinx/Vitis_Libraries.git
cd Vitis_Libraries
git sparse-checkout set vision/L1/include
```

Dacă biblioteca este deja descărcată **în versiunea 2022.2**, reutilizați directorul
`vision/L1/include` fără o nouă clonare. Fișierele sunt disponibile în
[ramura 2022.2 Vitis Libraries](https://github.com/Xilinx/Vitis_Libraries/tree/2022.2/vision/L1/include).

În **Vitis HLS 2022.2 Command Prompt** (CMD, nu PowerShell), folosind căile
de exemplu de mai sus:

```bat
cd /d C:\FPGA\Edge-Computing\Lab6\hardware\resize_hls
set "VITIS_VISION_INCLUDE=C:/FPGA/Vitis_Libraries/vision/L1/include"
vitis_hls -f build_resize.tcl
```

Aceasta rulează implicit doar **C Simulation**, nu sinteza. Testul verifică
64×48→32×24 și 32×24→16×12, cu imagine de intrare de culoare constantă.

**Rezultat așteptat:** în jurnal apar două rânduri `OK: ...`, apoi
`SIMULARE C REUSITA` și `CSim done` (formularea jurnalului poate varia).

Numai după confirmarea acestui rezultat rulăm **C Synthesis**:

```bat
set "LAB6_HLS_STAGE=csynth"
vitis_hls -f build_resize.tcl
```

Pentru export IP, doar după sinteza verificată:

```bat
set "LAB6_HLS_STAGE=export"
vitis_hls -f build_resize.tcl
```

## Criterii de validare înainte de Sobel

- C Simulation: două teste finalizate fără erori.
- C Synthesis: `resize_accel` sintetizat pentru `xc7z020clg400-1`, cu raport de resurse și latență.
- Export IP: interfețe `src` și `dst` AXI4-Stream, `s_axi_control` AXI-Lite.
- Testarea ulterioră în Vivado/PYNQ confirmă registrul, fluxurile și
  echivalența numerică față de Resize OpenCV.

**Nu există încă dovadă de compatibilitate prin sinteză pe mediul local.**
În caz de eroare, trimiteți primele mesaje CSim/Synthesis relevante;
modificăm doar ce indică mesajul, fără schimbări simultane speculative.

## Licență și proveniență

Sursa IP este adaptată din proiectul Xilinx/PYNQ-HelloWorld,
[BSD 3-Clause](https://github.com/Xilinx/PYNQ-HelloWorld/blob/master/LICENSE).
Vitis Vision este o dependență externă, neîncorporată în repository.
