#Nama:Ahmad Faiz
#pertemuan ke 12

1.
def buat_log():
 with open('log_kegiatan.txt', 'a') as file:
      kegiatan = input("masukan kegiatan yang baru saja anda lakukan:")
      file.write(kegiatan + '\n')
print("kegiatan telah di catat.")
jumlah_entri = int(input("berapa banyak entri yang ingin anda tambahkan?"))
for _ in range(jumlah_entri):
   buat_log()

2.
with open('sumber.txt', 'w') as file_sumber:
    file_sumber.write("Ini adalah baris pertama.\n")
    file_sumber.write("Ini adalah baris kedua.\n")
    file_sumber.write("Ini adalah baris ketiga.\n")
with open('sumber.txt', 'r') as file_sumber:
    isi = file_sumber.read() 
with open('salinan.txt', 'w') as file_salinan:
    file_salinan.write(isi) 
print("Proses penyalinan selesai.")

3.
import os

def hapus_file_aman():
    # Meminta input nama file dari pengguna
    nama_file = input("Masukkan nama file yang ingin dihapus: ")
    
    # Mengecek apakah file tersebut ada
    if not os.path.exists(nama_file):
        print(f"File '{nama_file}' tidak ditemukan.")
        return
    
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ")
    if konfirmasi.lower() == 'y':
        try:
            os.remove(nama_file)
            print(f"File '{nama_file}' berhasil dihapus.")
        except PermissionError:
            print("Error: Anda tidak memiliki izin untuk menghapus file ini.")
        except Exception as e:
            print(f"Error: {str(e)}")
    else:
        print("Penghapusan dibatalkan.")

hapus_file_aman()





