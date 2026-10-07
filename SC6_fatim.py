import json

print("Sistem Pencatatan Nilai Mahasiswa")


def input_wajib(pesan):
    data_pesan = input(pesan)
    while data_pesan.strip() == "":
        print("Input tidak boleh kosong.")
        data_pesan = input(pesan)

    return data_pesan.strip()

def input_angka(pesan):
    data_angka = input(pesan)
    while not data_angka.isdigit() or int(data_angka) <= 0:
        print("Input harus berupa angka lebih dari 0.")
        data_angka = input(pesan)
    return int(data_angka)

while True:
    print("=== MENU ===")
    print("1. Tampilkan Nilai Mahasiswa")
    print("2. Tambahkan Nilai Mahasiswa")
    print("3. Keluar")

    pilihan = input_angka("Pilih menu (1-3): ")

    if pilihan == 1:
        with open ("nilai.json", "r", encoding="utf-8") as n:
            nilai = json.load(n)
        print(nilai)

    elif pilihan == 2:
        nama_baru = input_wajib("masukkan nama: ")
        nim_baru = input_angka("masukkan nim: ")
        nilai_baru = input_angka("masukkan nilai:")
        data_baru = {
                "nama": nama_baru,
                "nim": nim_baru,
                "nilai": nilai_baru
                }
        
        nilai.append(data_baru)
        with open ("nilai.json", "w", encoding="utf-8") as n:
            json.dump(nilai, n, indent=4)

        print("Data berhasil ditambahkan.")


    elif pilihan == 3:
        print("Anda berhasil keluar.")
        break

        