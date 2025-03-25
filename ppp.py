while True:
    r = int(input("Masukkan jumlah baris kursi (minimal 4): "))
    c = int(input("Masukkan jumlah kolom kursi (minimal 4): "))
    if r >= 4 and c >= 4:
        break
    print("Ukuran minimal bioskop adalah 4x4! Silakan masukkan ulang.")

kursi = [str(i + 1) for i in range(r * c)]
#def tampilkan():
while True :
    print("\nLayout Kursi Bioskop:")
    for i in range(r):
        for j in range(c):
            nomor_kursi = i * c + j
            print(f"{kursi[nomor_kursi]:>3}", end=' ')
        print()

    pilih = int(input("\nMasukkan nomor kursi yang ingin dipesan (atau 0 untuk selesai): "))
    if pilih == 0:
        print("Terima kasih! Pemesanan selesai.")
        break
    if pilih < 1 or pilih > r*c :
        print("Nomor kursi tidak valid!")
        continue
    nomor_kursi = pilih - 1
    if kursi[nomor_kursi] == "X":
        print("Kursi sudah dipesan. Silakan pilih kursi lain.")
    else:
        kursi[nomor_kursi] = "X"
        print(f"Kursi {pilih} berhasil dipesan!")