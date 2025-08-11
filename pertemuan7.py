
#Nama:Ahmad Faiz
#pertemuan ke 7


#1.
#intstalisasi hitung mundur dari 10 ke 1
count = 10
while count > 0:
  print(count)
  count -=1
  print("blastoff!")

#2.
#game tebak angka sederhana
angka_rahasia = 1 #angka yang harus ditebak
while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("Selamat, tebakan anda benar!")
        break
    else:
        print("yahh gagall, coba lagi!")

print("Terima kasih sudah bermain!")

#3.
print("Selamat datang di program Input Angka Cerdas!")
print("Masukkan angka satu per satu.\n")

total = 0
count = 0

while True:
    user_input = input("Masukkan angka: ")

    if user_input.lower() == "done":
        break

    try:
        angka = float(user_input)
        total += angka
        count += 1
    except ValueError:
        print("Input tidak valid")
        continue

# Setelah loop selesai, hitung rata-rata
if count > 0:
    rata_rata = total / count
else:
    rata_rata = 0

# Tampilkan hasil
print("\n--- Hasil Perhitungan ---")
print("Total       :", total)
print("Jumlah Angka:", count)
print("Rata-rata   :", rata_rata)



     
   

  
