# Lab1 — Introducere în PYNQ și arhitectura Zynq

## Conectarea la placa PYNQ-Z2

### 1. Determinarea adresei IP

După pornirea plăcii, se verifică adresa IPv4 primită pe interfața Ethernet:

```bash
ip -4 addr show eth0
```

Adresa IP afișată se introduce în browser:

```text
http://<adresa_IP>
```

sau, pentru imaginile PYNQ care utilizează portul 9090:

```text
http://<adresa_IP>:9090
```

Parola implicită este `xilinx`.

### 2. Dacă adresa IP nu este corectă sau conexiunea nu funcționează

Pe card poate exista un **lease DHCP vechi**, memorat de la o rețea utilizată anterior.

Se șterge fișierul:

```bash
sudo rm /var/lib/dhcp/dhclient.eth0.leases
```

și se repornește placa:

```bash
sudo reboot
```

După repornire se verifică din nou:

```bash
ip -4 addr show eth0
```

și se testează noua adresă în browser.

### 3. Dacă placa nu primește în continuare o adresă IP

Se verifică configurația interfeței Ethernet:

```bash
sudo cat /etc/network/interfaces.d/eth0
```

Pentru obținerea automată a adresei prin DHCP configurația trebuie să conțină:

```text
auto eth0
iface eth0 inet dhcp
```

Dacă este necesar, fișierul poate fi editat cu:

```bash
sudo nano /etc/network/interfaces.d/eth0
```

După modificare se repornește placa:

```bash
sudo reboot
```

### 4. Variantă alternativă — conectare directă la calculator

1. Dacă **calculatorul gazdă** este conectat la rețea prin Wi-Fi, se activează opțiunea de partajare a conexiunii (**Sharing / Allow other network users to connect through this computer's Internet connection**) și conexiunea se partajează către adaptorul Ethernet la care este conectată placa PYNQ-Z2.

2. Se lansează **PuTTY** și se selectează o conexiune **Serial**. Portul serial al plăcii se identifică în **Device Manager**, iar viteza se setează la **115200 baud**.

3. În consola serială se verifică adresa IP primită de placă:

```bash
ip -4 addr show eth0
```

4. Adresa obținută se introduce în browser. Dacă este solicitată parola, se utilizează `xilinx`.

---

## Taskuri Lab1

- [Lab1.1 — Verificarea mediului PYNQ](./Lab1.1.ipynb)
