#Nama: Ahmad faiz
#pertemuan ke 10

1.
judul_input = input("Masukkan judul buku: ")
judul_bersih = judul_input.strip()
judul_standar = judul_bersih.title()
print("Judul yang telah distandarisasi:", judul_standar)

2.
email = input("Masukkan alamat email: ")
mengandung_at = "@" in email
akhiran_valid = email.endswith(".com") or email.endswith(".co.id")
if mengandung_at and akhiran_valid:
    print("Email valid")
else:
    print("Email tidak valid")

3.
kalimat = input("Masukkan kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")
kalimat_sesudah_sensor = kalimat.replace(kata_sensor, "***")
print("Hasil sensor:", kalimat_sesudah_sensor)

4.
nama_organisasi = input("Masukkan nama organisasi: ")
kata_kata = nama_organisasi.split()
akronim = ""
for kata in kata_kata:
    akronim += kata[0].upper()
print("Akronim:", akronim)

5.
import re 
judul = input("Masukkan judul artikel: ")
judul = judul.lower()
judul = judul.replace(" ", "-")
slug = re.sub(r'[^a-z0-9\-]', '', judul)
print("Slug URL:", slug)