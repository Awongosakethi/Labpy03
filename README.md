# Tugas Modul Praktikum 3

## Latihan 1
Pada latihan 1 kali ini kita akan mencari angka terkecil yang kurang dari 0,5. Berikut algoritma dan langkah-langkahnya:
##### A. Input 
 - Langkah pertama, kita harus membuat perintah untuk memasukan nilai N atau beberapa data yang diinginkan kita.
```
num = int(input("Masukan nilai N: "))
```
 - Langkah kedua, kita akan membuat variable untuk menentukan berapa jumlah data yang ingin di cari.
```
jumlah = num+1
start = 1
stop = jumlah
step = 1
```
##### B. Process
 - Langkah ketiga, kita menggunakan syntax looping for, untuk memulai dan mengakhiri looping sesuai input start, stop dan step yang sudah kita masukan di langkah sebelumnya.
```
for i in range(start, stop, step):
```
 - Langkah keempat, masukan perintah sebagai berikut dengan menggunakan fungsi random:
```
from random import random
    a = random()
```
##### C. Output 
 - Terakhir masukan perintah 'print' untuk menampilkan hasil dari input variable.
```
print("Data ke:",i,"=>",(a))
```
### Gambar hasil latihan 1
![latihan 1](https://user-images.githubusercontent.com/56240483/68085117-c61b1780-fe6f-11e9-90a8-3a1a0720c928.png)

## Latihan 2
Pada latihan 2 kali ini kita akan menampilkan bilangan terbesar dari N buah data yang diinpukan, dan angka 0 digunakan untuk berhenti. Berikut algoritma dan langkah-langkahnya:
##### A. Input
 - Pertama, masukan variable 'a' sebagai integer, kemudian menginputkan nilainya. Dan variable 'b' dengan nilai 0.
```
a = int()
b = 0
```
##### B. Process
 - Kedua, kita masukan syntax looping while apabila nilai 'a' kurang sama dengan 0, dan menginputkan program yang ingin kita looping.
```
while a >= 0:
    a = int(input("Masukan Bilangan: "))
```
 - Ketiga, inputkan If (kondisi 1) jika variable 'a' lebih besar dari variable 'b' dan variable 'b' sama dengan 'a', kemudian if (kondisi 2) jika variable 'a' sama dengan 0. Lalu kita menggunakan fungsi 'break' untuk menghentikan operasi dibawahnya jika suatu kondisi yang di tentukan sudah tercapai.
```
 if a > b:
        b = a
    if a == 0:
        break
```
##### C. Output
 - Terakhir, gunakan perintah 'print' mencetak bilangan terbesar.
```
print("Bilangan terbesar adalah", b)
```
### Gambar hasil latihan 2
![Latihan 2](https://user-images.githubusercontent.com/56240483/68085128-de8b3200-fe6f-11e9-91cc-b652f1a2f8f8.png)

## Program 1
Pada program 1 kali ini kita akan menghitung laba keuntungan per-bulan. Berikut algoritma dan langkah-langkahnya:
##### A. Input
 - Langkah pertama, kita membuat variable dengan nilai modal = 1000000000, nilai modal = 0, nilai untung = 0.
```
modal = 1000000000
laba = 0                                  
untung = 0
```
##### B. Process 
 - Selanjutnya menggunakan perulangan for, i dengan nilai awal 1 dan nilai akhir 9.
```
for i in range (1,9):
```
 - Lalu, masukan kondisi 1 apabila belum bulan ke-3 laba masih 0%, kondisi 2 apabila belum memasuki bulan ke-5 mendapat laba sebesar 1%, kondisi 3 apabila belum memasuki bulan ke-8 mendapat laba 5%, dan pada bulan ke-8 laba menurun 2%, maka laba bulan ke-8 sebesar 3%.
```
    if (i < 3):                  ## "if" = bila suatu kodisi tertentu tercapai maka apa yang harus dilakukan dengan fungsi ini kita bisa menjalankan sesuatu
        laba = 0
        untung = untung + laba
    elif(i < 5):                 ## "elif" = adalah ketika kondisi lainnya tercapai maka jalankan program.
        laba = modal*1/100
        untung = untung + laba
    elif(i < 8):
        laba = modal*5/100
        untung = untung + laba
    else:                        ## "else" = adalah ketika tidak ada suatu kondisi yang terpenuhi maka jalankan program.
        laba = modal*2/100
        untung = untung + laba
```
##### C. Output 
 - Terakhir gunakan perintah 'print' untuk mencetak laba perbulan dan mencetak total laba.
```
    print("Laba bulan ke", i, "sebesar:", laba)
print("Total laba adalah : ", untung)
```
### Gambar hasil program 1
![Program 1](https://user-images.githubusercontent.com/56240483/68085133-f498f280-fe6f-11e9-9223-ae06ec7f5a02.png)
