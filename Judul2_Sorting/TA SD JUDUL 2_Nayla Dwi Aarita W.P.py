
#Program mengurutkan nilai ujian mahasiswa

def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j] 
    arr[j] = temp 


def bubble_sort(arr, n): 
    for i in range(n - 1): 
        for j in range(n - i - 1): 
            if arr[j] < arr[j + 1]: 
                tukar(arr, j, j + 1) 


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print(f"Masukkan {n} nilai ujian mahasiswa:")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Nilai mahasiswa: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
                
    print(f"Daftar nilai sebelum diurutkan: {arr}")
    bubble_sort(arr, n)
    print("Daftar nilai setelah diurutkan (Bubble Sort):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main() 
    
    