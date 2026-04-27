def menu():
    print("MENU DESSERT")
    print("1. Tambahkan Dessert")
    print("2. Hapus Dessert")
    print("3. Tampilkan Dessert")
    print("4. Ubah Dessert")  
    print("5. Keluar")
 

def main():
    dessert = []

    while True:
        menu()
        try:
            pilihan = int(input("Pilihan menu (1-5): "))
        except ValueError:
            print("Masukkan angka yang valid")
            continue

        if pilihan == 1:
            nama = input("tambahkan nama dessert: ").strip().title()
            
            if nama:
                dessert.append(nama)
                print(f"'{nama}' berhasil ditambahkan.")
            else:
                print("Nama dessert tidak boleh kosong")

        elif pilihan == 2:
            nama = input("Masukkan nama dessert yang ingin dihapus: ").strip().title()
            
            if nama in dessert:
                dessert.remove(nama)
                print(f"'{nama}' berhasil dihapus.")
            else:
                print(f"'{nama}' tidak ditemukan dalam daftar.")

        elif pilihan == 3:
            if not dessert:
                print("Belum ada dessert yang ditambahkan.")
            else:
                print("Daftar Dessert:")
                for i, item in enumerate(dessert, 1):
                    print(f"   {i}. {item}")

        elif pilihan == 4:
            if not dessert:
                 print("Belum ada dessert yang bisa diubah.")
            else:
                nama_lama = input("Masukkan nama dessert yang ingin diubah: ").strip().title()
                
                if nama_lama in dessert:
                    nama_baru = input("tambahkan nama dessert yang baru: ").strip().title()
                    
                    if nama_baru:
                        indeks = dessert.index(nama_lama)
                        dessert[indeks] = nama_baru
                        print(f"'{nama_lama}' berhasil diubah menjadi '{nama_baru}'.")
                    else:
                        print("Nama dessert baru tidak boleh kosong")
                else:
                    print(f"'{nama_lama}' tidak ditemukan dalam daftar.")
                    
        elif pilihan == 5:
            print("Program selesai")
            break 

        else:
            print("Pilihan tidak valid! Silakan pilih angka 1-5.")

if __name__ == "__main__":
    main()