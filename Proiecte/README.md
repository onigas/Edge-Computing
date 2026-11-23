# Proiecte individuale — Edge Computing pe AMD Kria

[Înapoi la pagina cursului](../README.md)

## Obiectiv și organizare

Fiecare student reproduce **un proiect original din lista de mai jos**, pe placa Kria indicată, apoi implementează **extensia obligatorie** asociată. Lista conține **9 proiecte pentru KR260**, selectate din lista inițială pentru utilizarea imaginii Ubuntu existente și a overlay-urilor gata compilate. Numerele originale sunt păstrate. Lucrul și evaluarea sunt individuale; coloana „Student” rămâne liberă pentru repartizare.

**Durata: 4 săptămâni × 4 ore = 16 ore, inclusiv prezentările din săptămâna 4.** Primele trei sesiuni oferă 12 ore pentru reproducere, extensie și verificare. Nu se presupune o a cincea sesiune și nici muncă obligatorie suplimentară acasă.

## Condiții înainte de repartizare

**Se păstrează imaginea Ubuntu Kria instalată pe plăci.** Se pot instala bibliotecile, aplicațiile și containerele necesare și se pot încărca **numai overlay-uri deja compilate pentru KR260**. Nu se construiesc overlay-uri în Vivado/Vitis/HLS și nu se instalează PetaLinux, Yocto sau o imagine Ubuntu personalizată în locul celei existente. Extensiile se realizează în software, fără modificarea hardware-ului FPGA.

Versiunea Ubuntu, bibliotecile PYNQ/VART/XRT și modelele trebuie să fie compatibile cu pachetul precompilat ales. Verificarea documentației și a fișierelor publicate nu înlocuiește proba pe plăcile laboratorului. Dacă un pachet nu funcționează pe imaginea existentă, se alege altă temă din listă, fără reconstruirea overlay-ului sau înlocuirea imaginii.

Echipament comun: placa **KR260**, alimentator compatibil, card microSD cu imaginea Ubuntu existentă, PC pentru acces la placă, cabluri de rețea/USB necesare și conexiune la rețea. „Fără periferice” în tabel înseamnă fără periferice suplimentare față de acest echipament comun. Se verifică înainte și accesul la conturile, datele și pachetele software necesare.

Plăcile și perifericele partajate se programează pe intervale de utilizare. Codul, analiza și documentarea se pot pregăti pe PC în timpul aceleiași sesiuni; demonstrația și măsurătorile cerute se execută pe Kria. Repartizarea depinde de disponibilitatea efectivă a echipamentelor și a mediului validat.

## Lista proiectelor

### A. Interfețe, control, senzori și sisteme eterogene

| Nr. | Proiect original Hackster.io și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 5 | **[Control PWM DC Motor from PYNQ](https://www.hackster.io/iotengineer22/control-pwm-dc-motor-from-pynq-and-kr260-bb0296)** — comandă PWM a unui motor | Implementarea unei rampe de pornire și oprire (*soft-start/soft-stop*) | Motor DC, driver, alimentare | |

### B. Edge AI și procesare video pe Kria

| Nr. | Proiect original Hackster.io și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 9 | **[Edge Impulse on KR260](https://www.hackster.io/whitney-knitter/edge-impulse-on-kria-kr260-ed12bc)** — model ML propriu pentru recunoașterea obiectelor | Antrenarea a două clase de obiecte din laborator și evaluarea rezultatelor pe 20 de imagini noi | Cameră USB, cont Edge Impulse  | |
| 10 | **[RTSP Camera Source for Edge Impulse](https://www.hackster.io/whitney-knitter/rtsp-feed-camera-source-for-edge-impulse-on-kria-kr260-d47ec3)** — inferență din flux video IP | Adăugarea unui control al ratei de prelucrare (1, 2, 5 FPS) și compararea încărcării CPU | Cameră IP cu RTSP, model Edge Impulse pregătit  | |
| 11 | **[Object Detection with YOLOX + PYNQ](https://www.hackster.io/iotengineer22/object-detection-with-yolox-pynq-and-kr260-13d32f)** — detecție accelerată pe DPU | Înregistrarea într-un fișier CSV a obiectelor detectate, cu clasă, scor și timestamp | DPU/model pregătit; imagini de test, fără cameră obligatorie  | |
| 12 | **[Object Detection from a Webcam](https://www.hackster.io/iotengineer22/object-detection-with-kr260-from-a-webcam-85c261)** — detecție YOLOX în timp real | Salvarea automată a unei imagini atunci când apare o clasă selectată, cu limitarea alarmelor repetate | Cameră USB și DPU pregătit  | |
| 13 | **[Benchmark Architectures of the DPU](https://www.hackster.io/iotengineer22/benchmark-architectures-of-the-dpu-with-kr260-699f19)** — evaluarea configurațiilor DPU | Extinderea benchmarkului cu P50/P95 pentru latență, pe minimum trei configurații disponibile | Fără periferice; cel puțin 3 configurații DPU pregătite  | |
| 15 | **[Super Resolution Networks on KR260](https://www.hackster.io/beyond-the-game/deploy-the-super-resolution-networks-in-kr260-kit-0fe9c8)** — reconstruirea imaginilor folosind SRCNN/RDN | Comparație cu interpolarea bicubică, folosind PSNR, SSIM și timpul de execuție | Modele compilate și set de imagini  | |
| 16 | **[Forest Fire Prevention](https://www.hackster.io/takoeunice19/forest-fire-prevention-f5212c)** — clasificarea imaginilor cu incendii | Testarea pe imagini suplimentare cu și fără foc și generarea unei alarme la depășirea unui prag | Modelul CNN și date de test pregătite  | |
| 18 | **[EagleEye AI](https://www.hackster.io/matjaz4/eagleeye-ai-smart-following-camera-with-face-recognition-1b0f65)** — urmărirea feței cu ROS2 | Adăugarea unei zone moarte centrale pentru comanda pan-tilt, reducând oscilațiile | Cameră IP; mecanism pan-tilt/RS-485 pentru demonstrația fizică, sau verificarea comenzilor ROS2 fără motoare  | |

### Pachete de utilizat și precizări

- **Tema 5:** se descarcă fișierele `.bit`, `.hwh` și notebook-ul din [pachetul PWM al autorului](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/jupyter_notebooks/pynq-pwm). Se omit etapele de construire Vivado din articol. Extensia modifică secvența comenzilor PWM în Python.
- **Temele 9 și 10:** aplicații Edge Impulse pe Ubuntu, fără overlay FPGA propriu. Se instalează bibliotecile necesare; antrenarea/exportul modelului nu reprezintă construire de overlay. La tema 10 se raportează și rata efectiv realizată, nu doar rata solicitată.
- **Tema 11:** se folosesc overlay-ul și modelul din [pachetul YOLOX](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/src/yolox-test). Configurația originală include camera RICOH THETA V; varianta cu imagini pregătite reproduce inferența și extensia CSV, iar limitarea se menționează în raport.
- **Tema 12:** se folosesc fișierele `.bit`, `.hwh`, `.xclbin`, modelul și codul din [pachetul pentru cameră USB](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/src/usb-camera).
- **Tema 13:** [pachetul benchmark](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/jupyter_notebooks/pynq-benchmark) include configurații DPU și modele deja compilate. Se aleg minimum trei pachete complete și compatibile; nu se sintetizează alte configurații.
- **Tema 15:** se reutilizează overlay-ul DPU precompilat din mediul [Kria-RoboticsAI](https://github.com/amd/Kria-RoboticsAI), utilizat de autor, fără modificarea arhitecturii DPU. Modelele SRCNN/RDN trebuie să corespundă acestuia. Tema rămâne condiționată de disponibilitatea modelelor executabile și a bibliotecilor compatibile cu Ubuntu existent; extensia compară rezultatele în software.
- **Tema 16:** exemplul autorului folosește inferență CNN pe CPU în Ubuntu, fără overlay FPGA propriu. Sunt necesare bibliotecile Python și greutățile modelului. Disponibilitatea unui model gata de executat trebuie confirmată înainte de repartizare; articolul include cod de antrenare și testare, dar nu certifică existența modelului în laborator.
- **Tema 18:** se instalează [pachetul firmware precompilat](https://github.com/s59mz/eagle-eye-ai/tree/main/fpga-firmware) și aplicația Docker/ROS2 din repository-ul autorului, pe Ubuntu existent. Nu se parcurge reconstruirea hardware-ului din tutorial. Se poate verifica topicul ROS2 al comenzilor fără motoare; aceasta nu echivalează cu demonstrarea urmăririi fizice pan-tilt.
- Mențiunile anterioare privind portarea pe PYNQ-Z2 au fost retrase: ele presupuneau adaptarea sau regenerarea overlay-urilor, care nu intră în această selecție.

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
