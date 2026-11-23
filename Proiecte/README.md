# Proiecte individuale — Edge Computing pe AMD Kria

[Înapoi la pagina cursului](../README.md)

## Obiectiv și organizare

Fiecare student reproduce **un proiect original din lista de mai jos**, pe placa Kria indicată, apoi implementează **extensia obligatorie** asociată. Lista păstrează cele 20 de proiecte selectate: **1–19 pe KR260, 20 pe KV260**. Lucrul și evaluarea sunt individuale; coloana „Student” rămâne liberă pentru repartizare.

**Durata: 4 săptămâni × 4 ore = 16 ore, inclusiv prezentările din săptămâna 4.** Primele trei sesiuni oferă 12 ore pentru reproducere, extensie și verificare. Nu se presupune o a cincea sesiune și nici muncă obligatorie suplimentară acasă.

## Condiții înainte de repartizare

Proiectul original trebuie să fi fost pornit cu succes pe placa disponibilă înainte de repartizare. Nu se cere reconstruirea integrală a PetaLinux, a platformei FPGA sau a DPU de la zero în timpul celor patru sesiuni.

Echipament comun: placa **KR260** (temele 1–19) sau **KV260** (tema 20), alimentator compatibil, card microSD cu imaginea pregătită, PC pentru acces la placă, cabluri de rețea/USB necesare și conexiune la rețea. „Fără periferice” în tabel înseamnă fără periferice suplimentare față de acest echipament comun. Se verifică înainte și accesul la conturile, datele și pachetele software necesare.

Plăcile și perifericele partajate se programează pe intervale de utilizare. Codul, analiza și documentarea se pot pregăti pe PC în timpul aceleiași sesiuni; demonstrația și măsurătorile cerute se execută pe Kria. Repartizarea depinde de disponibilitatea efectivă a echipamentelor și a mediului validat.

## Lista proiectelor

### A. Interfețe, control, senzori și sisteme eterogene

| Nr. | Proiect original Hackster.io și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 1 | **[Vivado LED Control via PYNQ](https://www.hackster.io/wstanislaus/vivado-led-control-via-pynq-on-kr260-e391cf)** — comanda LED-urilor KR260 din Python | Interfață web simplă pentru selectarea a trei moduri de semnalizare LED | Fără periferice<br>**Realizabil și pe PYNQ-Z2**, cu adaptarea GPIO și a overlay-ului. | |
| 2 | **[PetaLinux GPIO Tutorial](https://www.hackster.io/LogicTronix/kria-kr260-petalinux-2022-2-gpio-tutorial-9b14bf)** — control GPIO din Linux | Aplicație Linux cu secvențe LED programabile și configurare prin argumente | Fără periferice<br>**Realizabil și pe PYNQ-Z2** pentru aplicația GPIO și extensie, cu adaptarea accesului GPIO; fluxul PetaLinux original necesită portare separată. | |
| 3 | **[FreeRTOS APU–RPU IPI](https://www.hackster.io/wstanislaus/freertos-led-control-kr260-apu-rpu-ipi-communication-2a35f6)** — comunicație între ARM A53 și R5 | Transmiterea unei comenzi numerice APU→RPU pentru modificarea perioadei LED, cu măsurarea timpului de răspuns | Fără periferice  | |
| 4 | **[MicroBlaze V + BMP180](https://www.hackster.io/LogicTronix/microblaze-v-on-kr260-with-bmp180-sensor-and-vitis-2025-1-35315c)** — citirea senzorului I²C pe RISC-V soft-core | Medierea a 10 măsurători și avertizare când temperatura depășește un prag | BMP180  | |
| 5 | **[Control PWM DC Motor from PYNQ](https://www.hackster.io/iotengineer22/control-pwm-dc-motor-from-pynq-and-kr260-bb0296)** — comandă PWM a unui motor | Implementarea unei rampe de pornire și oprire (*soft-start/soft-stop*) | Motor DC, driver, alimentare<br>**Realizabil și pe PYNQ-Z2**, cu adaptarea PWM și a pinilor. | |
| 6 | **[Driving Motors with Encoders](https://www.hackster.io/whitney-knitter/driving-motors-with-encoders-on-the-kria-kr260-ffb663)** — comandă motor și citire encoder | Menținerea unei turații impuse folosind un regulator proporțional simplu | Pmod HB3, motor N20 cu encoder<br>**Realizabil și pe PYNQ-Z2**, cu adaptarea și validarea PWM și a citirii encoderului. | |
| 7 | **[Sense HAT LED Matrix – Part II](https://www.hackster.io/LogicTronix/kria-kr260-rpi-sensehat-ledmatrix-on-petalinux-part-ii-d4c4e0)** — comandă matrice LED 8×8 | Afișarea grafică a temperaturii pe matrice, cu schimbarea culorii la prag | Raspberry Pi Sense HAT  | |
| 8 | **[Jumpstart KR260 with Sense HAT](https://www.hackster.io/LogicTronix/jumpstart-the-kr260-with-raspberry-pi-sensehat-petalinux-308dc5)** — senzori, LED-uri, joystick | Data logger pentru temperatură, umiditate și presiune, cu salvare CSV și statistici | Raspberry Pi Sense HAT  | |

### B. Edge AI și procesare video pe Kria

| Nr. | Proiect original Hackster.io și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 9 | **[Edge Impulse on KR260](https://www.hackster.io/whitney-knitter/edge-impulse-on-kria-kr260-ed12bc)** — model ML propriu pentru recunoașterea obiectelor | Antrenarea a două clase de obiecte din laborator și evaluarea rezultatelor pe 20 de imagini noi | Cameră USB, cont Edge Impulse  | |
| 10 | **[RTSP Camera Source for Edge Impulse](https://www.hackster.io/whitney-knitter/rtsp-feed-camera-source-for-edge-impulse-on-kria-kr260-d47ec3)** — inferență din flux video IP | Adăugarea unui control al ratei de prelucrare (1, 2, 5 FPS) și compararea încărcării CPU | Cameră IP cu RTSP, model Edge Impulse pregătit  | |
| 11 | **[Object Detection with YOLOX + PYNQ](https://www.hackster.io/iotengineer22/object-detection-with-yolox-pynq-and-kr260-13d32f)** — detecție accelerată pe DPU | Înregistrarea într-un fișier CSV a obiectelor detectate, cu clasă, scor și timestamp | DPU/model pregătit; imagini de test, fără cameră obligatorie  | |
| 12 | **[Object Detection from a Webcam](https://www.hackster.io/iotengineer22/object-detection-with-kr260-from-a-webcam-85c261)** — detecție YOLOX în timp real | Salvarea automată a unei imagini atunci când apare o clasă selectată, cu limitarea alarmelor repetate | Cameră USB și DPU pregătit  | |
| 13 | **[Benchmark Architectures of the DPU](https://www.hackster.io/iotengineer22/benchmark-architectures-of-the-dpu-with-kr260-699f19)** — evaluarea configurațiilor DPU | Extinderea benchmarkului cu P50/P95 pentru latență, pe minimum trei configurații disponibile | Fără periferice; cel puțin 3 configurații DPU pregătite  | |
| 14 | **[Vitis AI ONNX Runtime Engine](https://www.hackster.io/iotengineer22/vitis-ai-onnx-runtime-engine-voe-with-kr260-python-0d02c3)** — inferență ONNX pe CPU și DPU | Benchmark pe 30 de imagini: latență medie, P95 și verificarea concordanței predicțiilor CPU/DPU | Fără periferice; runtime și modele pregătite  | |
| 15 | **[Super Resolution Networks on KR260](https://www.hackster.io/beyond-the-game/deploy-the-super-resolution-networks-in-kr260-kit-0fe9c8)** — reconstruirea imaginilor folosind SRCNN/RDN | Comparație cu interpolarea bicubică, folosind PSNR, SSIM și timpul de execuție | Modele compilate și set de imagini  | |
| 16 | **[Forest Fire Prevention](https://www.hackster.io/takoeunice19/forest-fire-prevention-f5212c)** — clasificarea imaginilor cu incendii | Testarea pe imagini suplimentare cu și fără foc și generarea unei alarme la depășirea unui prag | Modelul CNN și date de test pregătite  | |
| 17 | **[WildSight AI](https://www.hackster.io/matjaz4/wildsight-ai-real-time-human-wildlife-conflict-detection-ff65fa)** — detectarea persoanelor și animalelor cu MegaDetector | Jurnalizarea evenimentelor cu om și animal detectați simultan, cu salvarea unui cadru relevant | Cameră USB/IP; imagine Docker și model pregătite  | |
| 18 | **[EagleEye AI](https://www.hackster.io/matjaz4/eagleeye-ai-smart-following-camera-with-face-recognition-1b0f65)** — urmărirea feței cu ROS2 | Adăugarea unei zone moarte centrale pentru comanda pan-tilt, reducând oscilațiile | Cameră IP; mecanism pan-tilt/RS-485 pentru demonstrația fizică, sau verificarea comenzilor ROS2 fără motoare  | |

### C. Procesare de semnal și accelerare FPGA

| Nr. | Proiect original Hackster.io și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 19 | **[Slaying the DMA Dragon on KR260](https://www.hackster.io/yuricauwerts/slaying-the-dma-dragon-on-the-kria-kr260-a5046e)** — modul Linux și transfer DMA pentru audio | Calculul și afișarea nivelului RMS pentru blocuri audio transmise prin DMA | Pmod I2S2; driver și proiect FPGA pregătite  | |
| 20 | **[FPGA FIR Filter – HLS/PYNQ pe KV260](https://www.hackster.io/michi_michi/fpga-fir-filter-hls-kria-kv260-pynq-2eec35)** — filtru FIR hardware cu date float/fixed-point | Modificarea coeficienților filtrului și compararea erorii numerice și a timpului de procesare | KV260, fără senzori; proiect HLS și overlay pregătite<br>**Realizabil și pe PYNQ-Z2**, cu regenerarea și validarea overlay-ului HLS/DMA pentru Zynq-7020. | |

### Precizări pentru alegerea temei

- Temele 7 și 8 folosesc același HAT, dar au obiective diferite: afișare, respectiv achiziție și înregistrare.
- La tema 11, configurația originală include camera RICOH THETA V. Varianta cu imagini pregătite reproduce partea de inferență și extensia CSV; această limitare trebuie menționată în raport.
- Tema 13 necesită cel puțin trei configurații DPU deja disponibile și validate; compilarea lor nu intră în timpul studentului.
- Temele 15–19 necesită pregătire atentă și se repartizează numai cu mediul funcțional și echipamentele confirmate. La tema 15 sunt necesare modelele compilate; la tema 16 trebuie confirmată disponibilitatea codului și a modelului CNN executabil. Lista nu certifică faptul că aceste pachete sunt deja disponibile în laborator.
- La tema 18 se poate evalua comanda ROS2 fără motoare, conform variantei selectate; aceasta nu echivalează cu demonstrarea urmăririi fizice pan-tilt. Varianta se stabilește de la început.
- Tema 19 presupune integrare DMA și driver Linux pregătite. Tema 20 se execută pe KV260, fără portare obligatorie pe KR260.
- Dacă o condiție nu este îndeplinită, se alege o altă temă disponibilă **din aceeași listă**, înainte de repartizare.

## Cerințe generale

1. Citiți proiectul original și identificați arhitectura, componentele hardware/software și fluxul datelor. Păstrați linkul către autor și respectați licențele codului reutilizat.
2. Reproduceți funcționalitatea de bază pe Kria și păstrați dovezi ale funcționării înainte de modificări. Documentați explicit eventualele limitări ale variantei acceptate.
3. Implementați extensia din tabel, separând clar codul preluat de contribuția proprie. Nu este suficientă schimbarea titlului, a culorilor sau simpla executare a exemplului.
4. Verificați reproductibil extensia: intrări/date de test, pași de rulare, rezultat așteptat și rezultat observat. Respectați numărul de imagini, configurațiile și metricile cerute în tema aleasă.
5. Includeți cel puțin un caz normal și un caz de limită relevant (prag, absența obiectului, comandă minimă/maximă etc.). Comparați varianta inițială cu extensia în aceleași condiții, prin comportament și/sau măsurători.
6. Pentru benchmarkuri precizați unitățile, numărul de repetări, configurația, pregătirea datelor și ce include timpul măsurat. Nu prezentați estimările sau rezultatele pe PC ca măsurători pe FPGA.
7. Predați codul și documentația până la finalul săptămânii 3. În săptămâna 4 explicați individual arhitectura, modificările și rezultatele și demonstrați proiectul.

## Calendar — 4 săptămâni × 4 ore

| Săptămâna | Activitate în cele 4 ore | Rezultat verificabil |
|---|---|---|
| **1 — Alegere și reproducere** | 30 min: confirmarea temei, echipamentului și extensiei; 45 min: studierea sursei și arhitecturii; 135 min: rularea și adaptarea exemplului în mediul pregătit; 30 min: salvarea dovezilor și identificarea problemelor. | Mediul pornește pe Kria; prima rulare a proiectului original și listă scurtă de probleme rămase. |
| **2 — Validarea bazei și extensie** | 60 min: finalizarea reproducerii; 30 min: teste și rezultate de referință; 120 min: implementarea extensiei; 30 min: demonstrație intermediară și salvarea codului. | Proiectul de bază funcțional, rezultate de referință și o primă versiune a extensiei. |
| **3 — Finalizare și predare** | 90 min: finalizarea extensiei; 75 min: teste și măsurători comparative; 60 min: README, raport și materialele demonstrației; 15 min: predarea versiunii finale. | Cod final, extensie verificată, rezultate, raport și demonstrație pregătită. |
| **4 — Prezentări și evaluare** | 15 min: organizare; până la 20 de prezentări × 10 min = 200 min; 25 min: rezervă pentru tranziții, probleme tehnice și feedback. | Prezentare individuală, demonstrație și răspunsuri la întrebări. |

O prezentare are **10 minute: 2 minute context/arhitectură, 4 minute demonstrație, 2 minute rezultate și contribuție proprie, 2 minute întrebări**. Pentru mai puțin de 20 de studenți, timpul rămas se folosește pentru discuții și feedback. Pentru mai mult de 20 de studenți, trebuie stabilite din timp grupe de evaluare separate care se încadrează fiecare în sesiunea de 4 ore. Săptămâna 4 nu este planificată ca sesiune de implementare.

## Livrabile

- **Codul sursă și configurația finală**, într-un repository sau o arhivă, cu versiune/commit identificabil, linkul sursei originale și modificările proprii explicate. Includeți notebook-urile/scripturile și fișierele de configurare necesare; pentru artefacte mari furnizați locația și versiunea.
- **README de reproducere**: placa și perifericele, schema de conectare unde este cazul, versiuni software, instalare, comenzi de rulare, intrări de test și rezultate așteptate. Nu includeți parole sau chei de acces.
- **Raport scurt, 2–4 pagini**: obiectiv, arhitectură, reproducerea proiectului original, extensie, metodologia testelor, rezultate comparative, limite și surse.
- **Dovezi și rezultate**: loguri/CSV, capturi, grafice sau alte ieșiri relevante temei; datele de test ori linkuri și instrucțiuni pentru obținerea lor. Includeți un scurt videoclip de rezervă al demonstrației pe Kria, util dacă apar probleme tehnice la prezentare.
- **Prezentarea din săptămâna 4**, cu demonstrația funcționalității de bază și a extensiei. Videoclipul de rezervă nu înlocuiește explicațiile individuale.

## Evaluare

| Componentă | Pondere | Ce se urmărește |
|---|---:|---|
| Reproducerea proiectului original | **50%** | Funcționare pe placa Kria indicată, respectarea variantei stabilite, înțelegerea arhitecturii și pași reproductibili. |
| Extensia proprie | **30%** | Îndeplinirea cerinței din tabel, integrarea corectă și demonstrarea contribuției individuale. |
| Testare, documentare și prezentare | **20%** | Teste și măsurători relevante, interpretarea rezultatelor, livrabile complete și răspunsuri clare la întrebări. |
| **Total** | **100%** | |

O rulare nemodificată a proiectului original nu obține punctajul extensiei. Rezultatele parțiale se documentează sincer și se evaluează în componentele corespunzătoare; citarea și delimitarea codului reutilizat sunt obligatorii.
