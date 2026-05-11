# NILAI UJIAN MAHASISWA

def sequential_search(data, n, target): 
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = [85, 90, 79, 88, 70, 95, 80, 85, 87, 92, 85, 76, 99, 87, 100]
    n = len(data)

    print(f"Data nilai ujian mahasiswa: {data}")

    while True:
        try:
            target = int(input("Masukkan nilai yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")

    counter = sequential_search(data, n, target)

    if counter > 0:
        print(f"Nilai {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Nilai {target} tidak ditemukan.")


if __name__ == "__main__":
    main()