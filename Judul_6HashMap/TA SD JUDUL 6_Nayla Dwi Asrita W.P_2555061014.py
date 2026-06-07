#Implementasi HashMap Separate Chaining untuk Pencarian Data Buku Berdasarkan Kode Buku

class Node:
    def __init__(self, kode_buku, judul_buku):
        self.key = kode_buku
        self.value = judul_buku
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nIsi Data Buku (Separate Chaining):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"({current.key}, {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    hashmap.insert(101, "Algoritma dan Pemrograman")
    hashmap.insert(111, "Struktur Data")
    hashmap.insert(121, "Basis Data")
    hashmap.insert(102, "Jaringan Komputer")
    hashmap.insert(187, "Kecerdasan Buatan")
    hashmap.display()

    hasil = hashmap.search(111)
    if hasil is not None:
        print(f"\nKode Buku {hasil.key} ditemukan")
        print(f"Judul Buku : {hasil.value}")
    else:
        print("\nBuku tidak ditemukan")

    hashmap.remove_key(111)
    print("\nSetelah menghapus kode buku 111:")
    hashmap.display()


if __name__ == "__main__":
    main()