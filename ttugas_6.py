
#Nama:Ahmad Faiz
#tugas ke 6

#1.
def buat_email(nama_pengguna, domain="ngaji.com"):
    return f"{nama_pengguna.lower()}@{domain.lower()}"
print(buat_email("faiz"))                # Output: faiz@ngaji.com
print(buat_email("jihat", "tutor.id"))   # Output: jihat@tutor.id

#2.
kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)


#3.
ef analisis_daftar(daftar_angka):
total = sum(daftar_angka)
jumlah_elemen = len(daftar_angka)
rata_rata = total / jumlah_elemen if jumlah_elemen != 0 else 0
return total, jumlah_elemen, rata_rata
data = [10, 20, 30, 40, 50]
total, jumlah, rata = analisis_daftar(data)

print("Total:", total)
print("Jumlah Elemen:", jumlah)
print("Rata-rata:", rata)


