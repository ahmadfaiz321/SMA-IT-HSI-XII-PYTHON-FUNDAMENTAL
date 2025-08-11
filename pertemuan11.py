while True:
     nama_file = input("masukan nama file(puisi.txt):")
     try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            print("Daftar Siswa (dibaca dengan 'with open'):")
            for baris in file:
                print(f"- {baris.strip()}")
     except FileNotFoundError as e:
        print(f"Error: File '{nama_file}' tidak ditemukan. Mohon periksa kembali.{e}")   


#2.
# nama_file_2 = input("Masukkan nama file (misalnya: mbox-short.txt): ")

# try:
#     with open(nama_file, 'r',encoding='utf-8') as file: # type: ignore
#         total = 0.0
#         count = 0

#         for baris in file:
#             if baris.startswith("X-DSPAM-Confidence:"):
#                 angka = float(baris.strip().split(":")[1])
#                 total += angka
#                 count += 1

#         if count > 0:
#             rata_rata = total / count
#             print(f"Rata-rata spam confidence: {rata_rata}")
#         else:
#             print("Tidak ada baris yang cocok ditemukan.")

# except FileNotFoundError:
#     print(f"File '{nama_file}' tidak ditemukan.") # type: ignore

# 3.
# while True:
#     nama_file = input("Masukkan nama file (contoh: puisi.txt): ")

#     if nama_file.lower() == "na na boo boo":
#         print("NA NA BOO BOO TO YOU - You have been punk'd!")
#         break

#     try:
#         with open(nama_file, 'r') as file:
#             print("Isi file dalam huruf kapital:")
#             for baris in file:
#                 print(baris.strip().upper())
#         break  

#     except FileNotFoundError:
#         print(f"Error: File '{nama_file}' tidak ditemukan. Coba lagi.")
