# Validare la pregatirea pachetului

Notebook-ul a trecut validarea nbformat si compilarea tuturor celulelor Python. Modulul auxiliar compileaza. Au trecut 10 teste software pentru hash, conversie BIN/PNG, pastrarea imaginii, intrari invalide, etichete, CSV, extragerea selectiva a arhivei, protectia de platforma si wrapper-ul de masurare.

```bash
python tests/test_lab71.py
```

Testele folosesc scoruri fictive numai pentru verificarea wrapper-ului, NU pentru verificarea modelului. Referinta binara are 3073 octeti si hash-ul sursei: `67a9b9e411d96725c170330073099269f9858ccc`.

**Nu au fost testate aici:** descarcarea runtime-ului pe placa, biblioteca ARM, programarea PL si inferenta pe PYNQ-Z2. Aceste verificari se efectueaza prin rularea notebook-ului. Modelul si rezultatele istorice din BNN-PYNQ nu sunt prezentate ca validare a acestui notebook. Nu sunt incluse rezultate FPGA precompletate.
