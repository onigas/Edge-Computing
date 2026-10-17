# Provenienta

Sursa: onigas/BNN-PYNQ, fork Xilinx/BNN-PYNQ. Commit: `d39c1c75403db571f54dd0f0cf27ae5104ac968e`.

`images/reference/deer.bin` este identic cu `tests/Test_image/deer.bin`: Git blob SHA-1 `67a9b9e411d96725c170330073099269f9858ccc`. PNG-ul se obtine fara pierderi din aceiasi pixeli. Antetul binar nu este eticheta reala a exemplului. Cerbul corespunde clasei 4 / Deer. Testul original pentru JPG este in `tests/test_qnn.py`.

JPG-ul optional are Git blob SHA-1 `6aaa046c4d58d87cd76eca728ec160e0b7a28db5`. Modelul, ponderile si bitstream-ul nu sunt regenerate. Preprocesarea si inferenta utilizeaza API-ul original. Alias-ul Pillow `Image.ANTIALIAS = Image.Resampling.LANCZOS`, daca este necesar, pastreaza algoritmul.

Referinte:
- https://github.com/onigas/BNN-PYNQ/blob/d39c1c75403db571f54dd0f0cf27ae5104ac968e/notebooks/CNV-QNN_Cifar10.ipynb
- https://github.com/onigas/BNN-PYNQ/blob/d39c1c75403db571f54dd0f0cf27ae5104ac968e/tests/test_qnn.py
- https://github.com/onigas/BNN-PYNQ/blob/d39c1c75403db571f54dd0f0cf27ae5104ac968e/bnn/bnn.py

## Licenta componentelor originale

Copyright (c) 2016, Xilinx, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
