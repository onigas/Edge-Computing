# Lab7 - Inferenta AI cu modele preantrenate

## [Lab7.1 - Clasificarea imaginilor din fisiere](Lab7.1.ipynb)

**PYNQ-Z2 / PYNQ 2.7.0 / CNV-W2A2 / CIFAR-10.**

Folosim reteaua, ponderile, biblioteca si bitstream-ul existente din [BNN-PYNQ](https://github.com/onigas/BNN-PYNQ/tree/d39c1c75403db571f54dd0f0cf27ae5104ac968e). Nu antrenam si nu reconstruim modelul. Lab1-Lab6 nu sunt modificate.

### Rulare

Copiati intregul director `Lab7` langa Lab1-Lab6. Deschideti `Lab7.1.ipynb` in Jupyter pe placa si executati celulele in ordine. Sunt necesare pachetele din imaginea PYNQ: PYNQ, NumPy, Pillow, matplotlib, cffi si IPython.

Opriti alte notebook-uri care programeaza FPGA-ul. Clasificatorul inlocuieste overlay-ul activ, dar nu modifica fisierele altor laboratoare.

Se foloseste mai intai instalarea `bnn` existenta. Daca lipseste, `ALLOW_DOWNLOAD=True` descarca sursa la commit-ul fixat si extrage componentele CNV-W2A2 deja construite in `_vendor/BNN-PYNQ`. Nu ruleaza pip, setup.py, sinteza sau antrenare. Prima descarcare necesita Internet; ulterior se foloseste copia locala. Nu descarcam setul CIFAR-10 complet.

Instalare din GitHub, din directorul care contine Lab1-Lab6:

```bash
curl -fL https://github.com/onigas/Edge-Computing/archive/refs/heads/main.tar.gz | tar -xz --strip-components=1 Edge-Computing-main/Lab7
```

Comanda extrage numai Lab7. Salvati datele personale inainte de actualizari ulterioare.

### Experimente

Testul de referinta utilizeaza `deer.bin` original si PNG-ul derivat fara pierderi. Sunt verificate scorurile BIN vs PNG si clasa asteptata Deer. Fotografia JPG exacta din testele originale poate fi descarcata optional, cu verificarea hash-ului.

Urmeaza o imagine JPG/PNG proprie, apoi un director de imagini etichetate si un benchmark fara afisare. Notebook-ul include trei sarcini pentru studenti.

### Imagini proprii si rezultate

Puneti JPG/PNG in `images/own/`. Etichetati prin subdirectoare numite `Cat`, `Dog`, `Truck` etc., sau prin `images/labels.csv`:

```csv
file,class_id
reference/deer.png,4
own/my_cat.jpg,3
own/my_truck.png,9
```

Clase: 0 Airplane, 1 Automobile, 2 Bird, 3 Cat, 4 Deer, 5 Dog, 6 Frog, 7 Horse, 8 Ship, 9 Truck. Imaginile fara eticheta nu intra in acuratete. Modelul nu detecteaza pozitii sau mai multe obiecte si nu are o clasa universala pentru necunoscute.

CSV-urile cu predictii si benchmark-ul, precum si `environment.json`, se genereaza in `results/`. Nu sunt incluse rezultate pretinse ca masurate pe placa.

### Offline si depanare

Referinta este inclusa. Pentru runtime folositi instalarea existenta sau descarcati pe PC [arhiva sursei fixate](https://github.com/onigas/BNN-PYNQ/archive/d39c1c75403db571f54dd0f0cf27ae5104ac968e.zip). Copiati continutul astfel incat sa existe `Lab7/_vendor/BNN-PYNQ/bnn/bnn.py`, alaturi de directoarele originale `bitstreams`, `libraries` si `params` din `bnn/`. Setati `ALLOW_DOWNLOAD=False`. Nu executati setup.py.

La eroare de biblioteca ARM sau de overlay, pastrati mesajul complet si opriti experimentul. Nu actualizati automat pachetele si nu treceti la software. Un apel C blocat poate necesita repornirea kernelului sau a placii; Interrupt nu este garantat. Daca alt notebook a incarcat un overlay, reporniti kernelul Lab7.1.

[Verificarile efectuate](VALIDATION.md) sunt software-only, nu inferenta pe FPGA. [Provenienta si licenta](THIRD_PARTY.md).
