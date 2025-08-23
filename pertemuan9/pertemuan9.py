
#Ahmad faiz
#pertemuan 9

1.
s= "belajar python itu menyenagkan"

#karakter pertama (B)
print("karakter pertama:",s[0])
#karakter terakhir (n)menggunakan indexing negatif
print("karakter terkahir:",s[-1])
#karakter spasi pertama (di indeks 7)
print("karakter spasi pertama:",s[7])

2.
s = "Belajar Python itu Menyenangkan"

# Substring "Python"
print("Substring 'Python':", s[8:14])

# Substring "Menyenangkan"
print("Substring 'Menyenangkan':", s[21:])

# Substring "Belajar"
print("Substring 'Belajar':", s[:7])

3.
 #Meminta pengguna memasukkan sebuah kata
kata = input("Masukkan sebuah kata: ")
# Menggunakan slicing untuk membalik kata
kata_terbalik = kata[::-1]

# Mencetak kata yang sudah dibalik
print("Kata setelah dibalik:", kata_terbalik)

# Mengecek apakah kata tersebut adalah palindrom
if kata.lower().replace(" ", "") == kata_terbalik.lower().replace(" ", ""):
    print("Ini adalah kata palindrom!")
else:
    print("Ini bukan kata palindrom.")

4.
# Kalimat panjang
kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

# Mengambil setiap karakter ketiga (mulai dari indeks 0)
kode_rahasia = kalimat[::3]
print("Kode rahasia:", kode_rahasia)

5.
#nama_salah = "dUDI sANTOSO"

nama_salah = "dUDI sANTOSO"
nama_depan = "B" + nama_salah[1:4].lower() #memperbaiki, dUDI -> Budi
nama_belakang = "S" + nama_salah[6:].lower() #memperbaiki sANTOSO -> Santoso
nama_benar = nama_depan + " " + nama_belakang #menggabungkan nama yg telah diperbaiki
print(nama_depan)
print(nama_belakang)
print("Nama yang sudah diperbaiki:", nama_benar)


