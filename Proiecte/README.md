# Proiecte individuale — Edge Computing pe AMD Kria

[Înapoi la pagina cursului](../README.md)

## Obiectiv și organizare

Fiecare student reproduce **un proiect original din lista de mai jos**, pe placa Kria indicată, apoi implementează **extensia obligatorie** asociată. Lista conține **16 teme din sursele discutate: 8 Hackster.io, 6 PYNQ Bootcamp și 2 din alte repository-uri GitHub**. Temele folosesc imaginea Ubuntu existentă și overlay-uri gata compilate sau rulează exclusiv în software. Fiecare temă indică placa și limitele variantei de reprodus. Lucrul și evaluarea sunt individuale; coloana „Student” rămâne liberă pentru repartizare.

**Durata: 4 săptămâni × 4 ore = 16 ore, inclusiv prezentările din săptămâna 4.** Primele trei sesiuni oferă 12 ore pentru reproducere, extensie și verificare. Nu se presupune o a cincea sesiune și nici muncă obligatorie suplimentară acasă.

## Condiții înainte de repartizare

**Se păstrează imaginea Ubuntu Kria instalată pe plăci.** Se pot instala bibliotecile, aplicațiile și containerele necesare și se pot încărca **numai overlay-uri deja compilate pentru placa aleasă (KR260 sau KV260)**. Nu se construiesc overlay-uri în Vivado/Vitis/HLS și nu se instalează PetaLinux, Yocto sau o imagine Ubuntu personalizată în locul celei existente. Extensiile se realizează în software, fără modificarea hardware-ului FPGA.

Versiunea Ubuntu, bibliotecile PYNQ/VART/XRT și modelele trebuie să fie compatibile cu pachetul precompilat ales. Verificarea documentației și a fișierelor publicate nu înlocuiește proba pe plăcile laboratorului. Dacă un pachet nu funcționează pe imaginea existentă, se alege altă temă din listă, fără reconstruirea overlay-ului sau înlocuirea imaginii.

Echipament comun: placa **KR260 sau KV260**, conform temei (PYNQ-Z2 este permisă numai unde este menționată explicit), alimentator compatibil, card microSD cu imaginea Ubuntu existentă, PC pentru acces la placă, cabluri de rețea/USB necesare și conexiune la rețea. „Fără periferice” în tabel înseamnă fără periferice suplimentare față de acest echipament comun. Se verifică înainte și accesul la conturile, datele și pachetele software necesare.

Plăcile și perifericele partajate se programează pe intervale de utilizare. Codul, analiza și documentarea se pot pregăti pe PC în timpul aceleiași sesiuni; demonstrația și măsurătorile cerute se execută pe placa indicată în temă. Repartizarea depinde de disponibilitatea efectivă a echipamentelor și a mediului validat.

## Lista proiectelor

### A. Edge AI și procesare video pe Kria

| Nr. | Proiect original și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 1 | **[Edge Impulse on KR260](https://www.hackster.io/whitney-knitter/edge-impulse-on-kria-kr260-ed12bc)** — model ML propriu pentru recunoașterea obiectelor | Antrenarea a două clase de obiecte din laborator și evaluarea rezultatelor pe 20 de imagini noi | Cameră USB, cont Edge Impulse  | S.B. și R.B. |
| 2 | **[RTSP Camera Source for Edge Impulse](https://www.hackster.io/whitney-knitter/rtsp-feed-camera-source-for-edge-impulse-on-kria-kr260-d47ec3)** — inferență din flux video IP | Adăugarea unui control al ratei de prelucrare (1, 2, 5 FPS) și compararea încărcării CPU | Cameră IP cu RTSP, model Edge Impulse pregătit  | |
| 3 | **[Object Detection with YOLOX + PYNQ](https://www.hackster.io/iotengineer22/object-detection-with-yolox-pynq-and-kr260-13d32f)** — detecție accelerată pe DPU | Înregistrarea într-un fișier CSV a obiectelor detectate, cu clasă, scor și timestamp | DPU/model pregătit; imagini de test, fără cameră obligatorie  | |
| 4 | **[Object Detection from a Webcam](https://www.hackster.io/iotengineer22/object-detection-with-kr260-from-a-webcam-85c261)** — detecție YOLOX în timp real | Salvarea automată a unei imagini atunci când apare o clasă selectată, cu limitarea alarmelor repetate | Cameră USB și DPU pregătit  | S.R., A.P. și T.G. |
| 5 | **[Benchmark Architectures of the DPU](https://www.hackster.io/iotengineer22/benchmark-architectures-of-the-dpu-with-kr260-699f19)** — evaluarea configurațiilor DPU | Extinderea benchmarkului cu P50/P95 pentru latență, pe minimum trei configurații disponibile | Fără periferice; cel puțin 3 configurații DPU pregătite  | |
| 6 | **[Super Resolution Networks on KR260](https://www.hackster.io/beyond-the-game/deploy-the-super-resolution-networks-in-kr260-kit-0fe9c8)** — reconstruirea imaginilor folosind SRCNN/RDN | Comparație cu interpolarea bicubică, folosind PSNR, SSIM și timpul de execuție | Modele compilate și set de imagini  | I.R., V.M. și C.A. |
| 7 | **[Forest Fire Prevention](https://www.hackster.io/takoeunice19/forest-fire-prevention-f5212c)** — clasificarea imaginilor cu incendii | Testarea pe imagini suplimentare cu și fără foc și generarea unei alarme la depășirea unui prag | Modelul CNN și date de test pregătite  | G.D. și M.R. |
| 8 | **[EagleEye AI](https://www.hackster.io/matjaz4/eagleeye-ai-smart-following-camera-with-face-recognition-1b0f65)** — urmărirea feței cu ROS2 | Adăugarea unei zone moarte centrale pentru comanda pan-tilt, reducând oscilațiile | Cameră IP; mecanism pan-tilt/RS-485 pentru demonstrația fizică, sau verificarea comenzilor ROS2 fără motoare  | O.M., B.C. și M.I. |

### Pachete de utilizat și precizări

- **Temele 1 și 2:** aplicații Edge Impulse pe Ubuntu, fără overlay FPGA propriu. Se instalează bibliotecile necesare; antrenarea/exportul modelului nu reprezintă construire de overlay. La tema 2 se raportează și rata efectiv realizată, nu doar rata solicitată.
- **Tema 3:** se folosesc overlay-ul și modelul din [pachetul YOLOX](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/src/yolox-test). Configurația originală include camera RICOH THETA V; varianta cu imagini pregătite reproduce inferența și extensia CSV, iar limitarea se menționează în raport.
- **Tema 4:** se folosesc fișierele `.bit`, `.hwh`, `.xclbin`, modelul și codul din [pachetul pentru cameră USB](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/src/usb-camera).
- **Tema 5:** [pachetul benchmark](https://github.com/iotengineer22/AMD-Pervasive-AI-Developer-Contest/tree/main/jupyter_notebooks/pynq-benchmark) include configurații DPU și modele deja compilate. Se aleg minimum trei pachete complete și compatibile; nu se sintetizează alte configurații.
- **Tema 6:** se reutilizează overlay-ul DPU precompilat din mediul [Kria-RoboticsAI](https://github.com/amd/Kria-RoboticsAI), utilizat de autor, fără modificarea arhitecturii DPU. Modelele SRCNN/RDN trebuie să corespundă acestuia. Tema rămâne condiționată de disponibilitatea modelelor executabile și a bibliotecilor compatibile cu Ubuntu existent; extensia compară rezultatele în software.
- **Tema 7:** exemplul autorului folosește inferență CNN pe CPU în Ubuntu, fără overlay FPGA propriu. Sunt necesare bibliotecile Python și greutățile modelului. Disponibilitatea unui model gata de executat trebuie confirmată înainte de repartizare; articolul include cod de antrenare și testare, dar nu certifică existența modelului în laborator.
- **Tema 8:** se instalează [pachetul firmware precompilat](https://github.com/s59mz/eagle-eye-ai/tree/main/fpga-firmware) și aplicația Docker/ROS2 din repository-ul autorului, pe Ubuntu existent. Nu se parcurge reconstruirea hardware-ului din tutorial. Se poate verifica topicul ROS2 al comenzilor fără motoare; aceasta nu echivalează cu demonstrarea urmăririi fizice pan-tilt.
- Temele Hackster din această selecție rămân pe KR260. Nu se transferă bitstream-uri Kria pe PYNQ-Z2. Pentru utilizarea plăcilor PYNQ-Z2 fără overlay nou, vedeți temele software 13 și 14.

## B. PYNQ Bootcamp — exemple existente cu extensie software

| Nr. | Proiect original și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 9 | **[PYNQ Bootcamp 401 — Crowd Estimation](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/self_paced/PYNQ%20401%20-%20Crowd%20Estimation)** — estimarea numărului de persoane din imagini cu modelul BCC gata compilat. | Alarmă la depășirea unui prag în trei imagini consecutive și export CSV; testați minimum 20 de imagini, comparând numărul estimat cu numărarea manuală. | KR260/KV260 cu DPU B4096 precompilat și `pt_BCC.xmodel`. Imagini de test; fără cameră sau LED bar obligatorie. Se omite afișarea Grove, conform precizărilor de mai jos. | |
| 10 | **[PYNQ Bootcamp 402 — Face Mask Detection](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/self_paced/PYNQ%20402%20-%20Face%20Mask%20Detection)** — detecția măștilor cu modelul yolo-fastest furnizat. | Comparați trei praguri de încredere pe aceleași 20 de imagini etichetate manual și exportați numărul de detecții corecte, false și omise. | KR260/KV260, DPU B4096 precompilat, `pt_face-mask-detection.xmodel`; imagini de test. Cameră USB opțională. | |
| 11 | **[PYNQ Bootcamp 403 — Automotive / ENet](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/self_paced/PYNQ%20403%20-%20Automotive)** — segmentarea semantică a imaginilor rutiere cu modelul ENet furnizat. | Calculați procentul de pixeli al clasei „drum” într-o regiune selectată și salvați rezultatele pentru 20 de imagini; demonstrați efectul schimbării regiunii, fără reantrenare. | KR260/KV260, DPU B4096 precompilat și `pt_ENet.xmodel`; imagini rutiere. Se păstrează partea de segmentare, fără exercițiul final cu Base Overlay/Grove. | |
| 12 | **[PYNQ Bootcamp 503 — Pose Detection](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/PYNQ%20503%20-%20Pose%20Detection%20(Breakout%202))** — inferență OpenPose și vizualizarea hărților de probabilitate ale articulațiilor. | Adăugați selectarea unei articulații și afișarea poziției maximului și a scorului; aplicați un prag pentru rezultatele nesigure și exportați coordonatele pentru 20 de cadre cu o singură persoană. | KR260/KV260, DPU B4096 precompilat, `openpose_pruned_0_3.xmodel`; imagini sau cameră USB. Extensia nu cere reconstruirea scheletului pentru mai multe persoane. | |
| 13 | **[PYNQ Bootcamp 501 — Computer Vision](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/PYNQ%20501%20-%20Computer%20Vision%20(Breakout%202))** — prelucrare OpenCV, inclusiv detectarea markerelor ArUco și citirea codurilor QR. | Extindeți exemplul ArUco cu jurnal CSV (ID, centru în imagine, timestamp) și eliminarea raportărilor repetate într-un interval configurabil; verificați 20 de cadre cu markere prezente/absente. | KR260/KV260; **realizabil și pe PYNQ-Z2**, în software, fără overlay nou. OpenCV cu modul ArUco; markere tipărite și cameră USB sau imagini salvate. | T.G., D.L. și B.G. |
| 14 | **[PYNQ Bootcamp 504 — Board-to-Board Communication](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/PYNQ%20504%20-%20Board%20to%20Board%20Communication)** — mesagerie HTTP prin serverul și biblioteca `pynqp2p` furnizate. | Adăugați identificator de mesaj, confirmare și timeout; măsurați RTT pentru 100 de mesaje și raportați pierderile/confirmările lipsă într-un CSV. | O placă KR260/KV260 sau **PYNQ-Z2**, fără overlay; PC în aceeași rețea pentru server și al doilea client de test. Se reproduce partea de mesagerie, fără extensia opțională cu senzori. Lucru individual, fără două plăci obligatorii. | K.A. și C.M. |

### Utilizarea Bootcamp pe imaginile existente

- Se descarcă notebook-urile și fișierele asociate din [repository-ul PYNQ Bootcamp](https://github.com/Xilinx/PYNQ_Bootcamp), **fără instalarea imaginii SD Bootcamp**.
- Bootcamp este documentat în primul rând pentru **KV260**. Pentru temele 9–12, utilizarea pe **KR260** se bazează pe overlay-ul **DPU-PYNQ B4096 precompilat pentru KR260**, nu pe copierea bitstream-ului KV260. Ambele plăci sunt listate în [DPU-PYNQ](https://github.com/Xilinx/DPU-PYNQ), iar [Kria-PYNQ](https://github.com/Xilinx/Kria-PYNQ#included-overlays) instalează DPU pe Ubuntu pentru ambele.
- Modelele `.xmodel` sunt prezente în directoarele temelor. Compatibilitatea model–DPU–runtime se verifică la prima rulare; existența fișierului nu înseamnă că a fost testat pe plăcile laboratorului. Pentru această familie de exemple se urmărește mediul documentat **PYNQ 3.0 / Vitis AI 2.5**, fără amestecarea necontrolată cu pachetele Vitis AI 3.5 ale altor teme.
- În tema 9 se elimină numai celulele de inițializare și afișare Grove/LED bar (`PmodGroveAdapter`, `overlay.PMODA`); în tema 11 se omite exercițiul periferic de la final. Inferența și extensiile rămân. Acestea sunt adaptări software; nu se modifică overlay-ul.
- Temele 13 și 14 rulează pe CPU și nu folosesc DPU. De aceea pot utiliza și **PYNQ-Z2**, cu bibliotecile Python/OpenCV compatibile instalate. La tema 14, [serverul și clientul de test](https://github.com/Xilinx/PYNQ_Bootcamp/tree/master/bootcamp_sessions/PYNQ%20504%20-%20Board%20to%20Board%20Communication/pynq-p2p) sunt deja furnizate.
- Exemplele generale Python și MNIST nu sunt teme suplimentare aici, pentru a nu repeta pur și simplu laboratoarele deja parcurse. La Computer Vision contribuția evaluată este extensia ArUco, nu doar conversia grayscale/resize.

## C. Alte proiecte GitHub din sursele discutate

| Nr. | Proiect original și descriere | Extensia obligatorie | Echipament suplimentar / mediu necesar | Student |
|---|---|---|---|---|
| 15 | **[Robotics Base Platform — exemplul PWM](https://github.com/NotBlackMagic/RoboticsBasePlatform-KR260/blob/master/Python/Examples/TestPWM.py)** — controlul AXI Timer din Python folosind driverul și hardware-ul deja publicate. | Adăugați limite configurabile pentru comandă și un watchdog software care readuce PWM la o valoare sigură dacă nu mai sosesc comenzi; demonstrați comanda normală, depășirea limitelor și timeout-ul. | KR260; pachetul precompilat `kr260_pixhawk_v2`, driverul `DriverPWM.py`, analizor logic/osciloscop pentru verificarea semnalului; servomotor și alimentare doar dacă se demonstrează mișcarea. Tema acoperă modulul PWM, nu robotul complet. | |
| 16 | **[STAR-Bench / ETNA — înregistrarea imaginilor](https://github.com/necst/STAR-Bench/tree/main/ETNA)** — alinierea a două imagini prin informație mutuală, cu overlay-ul ETNA publicat. | Adăugați un experiment reproductibil pe 10 perechi de imagini cu translații cunoscute: comparați CPU/FPGA, timpul de execuție și eroarea translației estimate, cu export CSV. | KR260/KV260 conform platformelor declarate de autor; `ETNA/etna.bit` și `etna.hwh`, PYNQ, OpenCV/PyTorch și imagini 256×256. Fără senzori; se folosește numai ETNA/MI cu un optimizator, fără întregul benchmark și fără modele suplimentare. | |

### Fișiere gata de utilizat și limitele temelor GitHub

- **Tema 15:** exemplul `TestPWM.py` referă `kr260_pixhawk_v2`. Pachetul corespunzător, cu `.bit`, `.hwh` și `.dtbo`, există în [ROS/ros2_ws/src/locomotion/kr260_pixhawk_v2](https://github.com/NotBlackMagic/RoboticsBasePlatform-KR260/tree/master/ROS/ros2_ws/src/locomotion/kr260_pixhawk_v2). Se adaptează calea din script și se încarcă pachetul înainte de accesul la registre (`download=False` presupune hardware deja încărcat). Se folosește driverul original și maparea pinilor din proiect. Nu se construiește un overlay nou și nu se folosește varianta `kr260_pixhawk_v3_dpu`, semnalată de autor ca problematică.
- **Tema 16:** fișierele `etna.bit` și `etna.hwh` sunt incluse în [ETNA](https://github.com/necst/STAR-Bench/tree/main/ETNA). Reproducerea se limitează la exemplul minimal ETNA și la comparația CPU/FPGA. **Se verifică explicit că acceleratorul este activ:** codul autorului poate reveni automat la CPU dacă încărcarea FPGA eșuează; o asemenea rulare nu se raportează drept rezultat FPGA.
- Selecția include variante delimitate ale proiectelor existente, nu implementarea integrală a unor platforme robotice sau de cercetare. Nu se cere portarea hardware pe altă placă.

## Cerințe generale

1. Citiți proiectul original și identificați arhitectura, componentele hardware/software și fluxul datelor. Păstrați linkul către autor și respectați licențele codului reutilizat.
2. Reproduceți funcționalitatea de bază pe placa indicată în temă și păstrați dovezi ale funcționării înainte de modificări. Documentați explicit eventualele limitări ale variantei acceptate.
3. Implementați extensia din tabel, separând clar codul preluat de contribuția proprie. Nu este suficientă schimbarea titlului, a culorilor sau simpla executare a exemplului.
4. Verificați reproductibil extensia: intrări/date de test, pași de rulare, rezultat așteptat și rezultat observat. Respectați numărul de imagini, configurațiile și metricile cerute în tema aleasă.
5. Includeți cel puțin un caz normal și un caz de limită relevant (prag, absența obiectului, comandă minimă/maximă etc.). Comparați varianta inițială cu extensia în aceleași condiții, prin comportament și/sau măsurători.
6. Pentru benchmarkuri precizați unitățile, numărul de repetări, configurația, pregătirea datelor și ce include timpul măsurat. Nu prezentați estimările sau rezultatele pe PC ca măsurători pe FPGA.
7. Predați codul și documentația până la finalul săptămânii 3. În săptămâna 4 explicați individual arhitectura, modificările și rezultatele și demonstrați proiectul.

## Calendar — 4 săptămâni × 4 ore

| Săptămâna | Activitate în cele 4 ore | Rezultat verificabil |
|---|---|---|
| **1 — Alegere și reproducere** | 30 min: confirmarea temei, echipamentului și extensiei; 45 min: studierea sursei și arhitecturii; 135 min: rularea și adaptarea exemplului în mediul pregătit; 30 min: salvarea dovezilor și identificarea problemelor. | Mediul pornește pe placa aleasă; prima rulare a proiectului original și listă scurtă de probleme rămase. |
| **2 — Validarea bazei și extensie** | 60 min: finalizarea reproducerii; 30 min: teste și rezultate de referință; 120 min: implementarea extensiei; 30 min: demonstrație intermediară și salvarea codului. | Proiectul de bază funcțional, rezultate de referință și o primă versiune a extensiei. |
| **3 — Finalizare și predare** | 90 min: finalizarea extensiei; 75 min: teste și măsurători comparative; 60 min: README, raport și materialele demonstrației; 15 min: predarea versiunii finale. | Cod final, extensie verificată, rezultate, raport și demonstrație pregătită. |
| **4 — Prezentări și evaluare** | 15 min: organizare; până la 20 de prezentări × 10 min = 200 min; 25 min: rezervă pentru tranziții, probleme tehnice și feedback. | Prezentare individuală, demonstrație și răspunsuri la întrebări. |

O prezentare are **10 minute: 2 minute context/arhitectură, 4 minute demonstrație, 2 minute rezultate și contribuție proprie, 2 minute întrebări**. Pentru mai puțin de 20 de studenți, timpul rămas se folosește pentru discuții și feedback. Pentru mai mult de 20 de studenți, trebuie stabilite din timp grupe de evaluare separate care se încadrează fiecare în sesiunea de 4 ore. Săptămâna 4 nu este planificată ca sesiune de implementare.

## Livrabile

- **Codul sursă și configurația finală**, într-un repository sau o arhivă, cu versiune/commit identificabil, linkul sursei originale și modificările proprii explicate. Includeți notebook-urile/scripturile și fișierele de configurare necesare; pentru artefacte mari furnizați locația și versiunea.
- **README de reproducere**: placa și perifericele, schema de conectare unde este cazul, versiuni software, instalare, comenzi de rulare, intrări de test și rezultate așteptate. Nu includeți parole sau chei de acces.
- **Raport scurt, 2–4 pagini**: obiectiv, arhitectură, reproducerea proiectului original, extensie, metodologia testelor, rezultate comparative, limite și surse.
- **Dovezi și rezultate**: loguri/CSV, capturi, grafice sau alte ieșiri relevante temei; datele de test ori linkuri și instrucțiuni pentru obținerea lor. Includeți un scurt videoclip de rezervă al demonstrației pe placa aleasă, util dacă apar probleme tehnice la prezentare.
- **Prezentarea din săptămâna 4**, cu demonstrația funcționalității de bază și a extensiei. Videoclipul de rezervă nu înlocuiește explicațiile individuale.

## Evaluare

| Componentă | Pondere | Ce se urmărește |
|---|---:|---|
| Reproducerea proiectului original | **50%** | Funcționare pe placa indicată în temă, respectarea variantei stabilite, înțelegerea arhitecturii și pași reproductibili. |
| Extensia proprie | **30%** | Îndeplinirea cerinței din tabel, integrarea corectă și demonstrarea contribuției individuale. |
| Testare, documentare și prezentare | **20%** | Teste și măsurători relevante, interpretarea rezultatelor, livrabile complete și răspunsuri clare la întrebări. |
| **Total** | **100%** | |

O rulare nemodificată a proiectului original nu obține punctajul extensiei. Rezultatele parțiale se documentează sincer și se evaluează în componentele corespunzătoare; citarea și delimitarea codului reutilizat sunt obligatorii.
