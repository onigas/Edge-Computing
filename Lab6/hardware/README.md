# Lab6.2 — Specificația implementării hardware pe PYNQ-Z2

**Stadiu (octombrie 2026):** overlay-ul experimental Resize → Grayscale → Sobel a fost generat, iar perechea `Lab6/overlay/resize_sobel.bit` / `resize_sobel.hwh` este publicată. Validarea funcțională pe PYNQ-Z2 rămâne de efectuat și de documentat prin `Lab6.2_FPGA.ipynb` (variantele A, B, C).

Overlay-ul din Lab5 implementează doar Resize. Nu poate fi utilizat drept overlay **Resize → Sobel** fără refacerea și verificarea proiectului FPGA.

## Etapă istorică — pregătirea Resize pentru Vitis 2022.2

Am pregătit [sursele și testbench-ul Resize](resize_hls/README.md) în
`Lab6/hardware/resize_hls/`. Prima verificare se face prin **C Simulation**
în Vitis HLS 2022.2 pe PC, înainte de sinteza IP-ului și înainte de
integrarea Sobel în Vivado. Textul acestei secțiuni descrie etapa inițială; între timp a fost generată și publicată o pereche experimentală bit/hwh pentru pipeline-ul complet.

---

## 1. Arhitectura urmărită

```text
         Zynq PS / Python / DDR
                   |
              AXI4-MM (HP)
                   |
              AXI DMA MM2S
                   |
               AXI4-Stream
                   |
              Resize (HLS)
                   |
           Conversie BGR/RGB
             la grayscale
                   |
          Sobel 3×3 + linii
                   |
               AXI4-Stream
                   |
              AXI DMA S2MM
                   |
              AXI4-MM (HP)
                   |
           Rezultat în DDR
```

**AXI-Lite** configurează registrele (dimensiuni, pornire, stare).
**AXI4-Stream** transportă pixelii între IP-uri.
**AXI4-MM**, prin interfața HP, permite accesul DMA la DDR.

Trebuie verificate domeniile de ceas, semnalele de reset și comunicația dintre blocuri.

## 2. Ce trebuie verificat în IP-ul Resize existent

Înainte de proiectarea noului overlay analizăm fișierul HWH al acceleratorului și interfața sa HLS/RTL:

1. Lățimea efectivă `TDATA` la intrare și la ieșire.
2. Ordinea canalelor BGR sau RGB și formatul pixelilor.
3. Registrele de control și dimensiunile `src_rows`, `src_cols`, `dst_rows`, `dst_cols`.
4. Semnificația `TLAST`, `TUSER`, `TKEEP`.
5. Lungimea transferurilor DMA și delimitarea pachetelor.
6. Comportamentul în condiții de backpressure (`TVALID/TREADY`).

Nu presupunem că o imagine BGR de 24 biți implică automat o magistrală AXI-Stream de 24 biți. În AXI4-Stream Video, `TLAST` marchează frecvent sfârșitul liniei, iar tratarea sa trebuie corelată cu DMA-ul.

## 3. Definiția algoritmului Sobel

Pentru o comparație numerică riguroasă cu Lab4 și Lab6:

- Imagine de intrare grayscale uint8.
- Nuclee Sobel 3×3 pentru gradientele `Gx` și `Gy`.
- Politică explicită pentru pixelii de la margini.
- Magnitudine `sqrt(Gx² + Gy²)`, rotunjire și saturare la uint8.

**Important:** în Lab6.2 modelul cu trei linii folosește `BORDER_CONSTANT`, iar funcția software standard din Lab4 folosește, implicit, politica de margini OpenCV. La verificare trebuie selectată aceeași politică pentru ambele trasee.

Înlocuirea magnitudinii L2 cu `|Gx| + |Gy|`, cuantizarea diferită sau pragurile binare schimbă algoritmul. Aceste variante sunt posibile, dar trebuie cuantificate diferențele.

## 4. Pași de implementare în Vivado/Vitis 2022.2

1. Identificăm sursa HLS Resize compatibilă cu Vivado/Vitis 2022.2.
2. Proiectăm conversia grayscale și nucleul Sobel cu fereastră 3×3 și buffere de linii.
3. Scriem teste unitare pentru dimensiuni mici, margini și opriri `TREADY=0`.
4. Construim schema Vivado cu AXI DMA, AXI-Lite, interconectare, ceas și reset.
5. Verificăm lățimea `TDATA`, `TKEEP`, `TLAST`, `TUSER` și lungimea ieșirii DMA.
6. Executăm sinteza și implementarea; analizăm resursele LUT/FF/BRAM/DSP și închiderea constrângerilor temporale.
7. Exportăm **perechea corespunzătoare** `resize_sobel.bit` și `resize_sobel.hwh`.
8. În PYNQ inspectăm `overlay.ip_dict` și identificăm IP-urile și adresele fără hardcodare.
9. Validăm numeric imaginile procesate înainte de orice benchmark.
10. Măsurăm separat DMA+PL, întregul traseu de procesare și aplicația video end-to-end.

**Criterii de acceptare propuse:** 30 de cadre consecutive fără blocarea DMA, dimensiuni corecte, erori numerice cuantificate și măsurători reproductibile.

## 5. Variante experimentale

| Configurație | Cadru intermediar în DDR? | Stadiu |
| --- | --- | --- |
| Resize → Sobel integral pe ARM | Buffer software | Executabil |
| Resize în PL → Sobel pe ARM | Da, prin DMA | Executabil cu Lab5 |
| Resize în PL → DDR → Sobel în PL | Da | Overlay experimental disponibil; test hardware necesar |
| Resize → Sobel conectate direct în PL | Nu, doar buffere locale de linii | Necesită un nou design |

Reducerea traficului DDR calculată în Lab6.2 este un **model analitic**, nu o măsurătoare a controlerului de memorie.

## 6. Proiecte de referință

- PYNQ-HelloWorld: https://github.com/Xilinx/PYNQ-HelloWorld
- PYNQ Composable Pipeline: https://github.com/Xilinx/PYNQ_Composable_Pipeline

Acestea pot constitui puncte de plecare pentru proiectare, dar nu furnizează direct o pereche validată `resize_sobel.bit` / `resize_sobel.hwh` pentru configurația laboratorului.
