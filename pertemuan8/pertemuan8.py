
#Nama:Ahmad Faiz
#pertemuan ke 8


#1.
for i in range(0, 71, 7):
    print(i)


#2.
kalimat = "Python"

kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik
    
print(kalimat_terbalik)



3.
jumlah = 0
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        jumlah +=1
        print("jumlah angka yang habis di bagi")

#4.print("jumlah angka yang habis di bagi 3 dan 5 dari 1 sampai 50 adalah:", count)

#(4)
for i in range (5, 0, -1):      #Loop dari 5 ke 1 (mundur)
    for j in range (i):         # Loop untuk mencetak '*' sebanyak i kali
        print('*' ,end='')      # Cetak '*' tanpa pindah baris
    print()                     #Pindah ke baris berikutnya setelah satu baris selesai

#5
angka = int(input("Masukkan bilangan bulat positif: "))

if angka < 0:
    print("Maaf, faktorial hanya bisa dihitung untuk bilangan bulat positif.")
else:
    # Inisialisasi akumulator
    hasil_faktorial = 1

    # Perulangan dari 1 sampai angka
    for i in range(1, angka + 1):
        hasil_faktorial *= i  # akumulasi perkalian

    #  hasil
    print(f"Faktorial dari {angka} adalah {hasil_faktorial}")

    