# Program menentukan jumlah hari dalam bulan menggunakan perulangan while

print("Program Jumlah Hari dalam Bulan")
ulang = "y"

while ulang.lower() == "y":
    tahun = int(input("Masukkan tahun (misal: 2024): "))
    bulan = int(input("Masukkan nomor bulan (1-12): "))

    if bulan == 1:
        nama_bulan = "Januari"
        hari = 31
    elif bulan == 2:
        nama_bulan = "Februari"
        # Mengecek tahun kabisat
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            hari = 29
        else:
            hari = 28
    elif bulan == 3:
        nama_bulan = "Maret"
        hari = 31
    elif bulan == 4:
        nama_bulan = "April"
        hari = 30
    elif bulan == 5:
        nama_bulan = "Mei"
        hari = 31
    elif bulan == 6:
        nama_bulan = "Juni"
        hari = 30
    elif bulan == 7:
        nama_bulan = "Juli"
        hari = 31
    elif bulan == 8:
        nama_bulan = "Agustus"
        hari = 31
    elif bulan == 9:
        nama_bulan = "September"
        hari = 30
    elif bulan == 10:
        nama_bulan = "Oktober"
        hari = 31
    elif bulan == 11:
        nama_bulan = "November"
        hari = 30
    elif bulan == 12:
        nama_bulan = "Desember"
        hari = 31
    else:
        print("Nomor bulan tidak valid!")
        hari = None

    if hari:
        print(f"Bulan {nama_bulan} tahun {tahun} memiliki {hari} hari.")

    # Tanya user apakah ingin mengulangi
    ulang = input("Apakah ingin cek lagi? (y/n): ")

print("Program selesai. Terima kasih!")
