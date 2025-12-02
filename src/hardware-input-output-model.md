# Model Arsitektur Input–Output (I/O)

Sistem I/O pada komputer terdiri dari:

## 1. Input Device
Perangkat yang mengirimkan data ke komputer, contoh: keyboard.

## 2. CPU
CPU melakukan:
- Fetch data dari input buffer
- Decode dan process
- Store ke output buffer

## 3. Register
Di dalam CPU, data melewati:
- Register MAR (Memory Address Register)
- Register MDR (Memory Data Register)
- ACC (Accumulator) untuk pengolahan

## 4. Output Device
Menampilkan hasil di layar.

## 5. Mekanisme I/O
Tiga jenis:
- Programmed I/O
- Interrupt-driven I/O
- DMA (Direct Memory Access)

Project ini menggunakan programmed I/O, yaitu CPU menunggu input lalu memprosesnya.
