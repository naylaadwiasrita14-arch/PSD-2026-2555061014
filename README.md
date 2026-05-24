**SISTEM PENYIMPANAN DATA NOMOR KONTAK**

Program ini dirancang untuk menyimpan data nomor kontak yang dapat dimasukkan oleh pengguna. Pengguna akan diminta memasukkan nama beserta nomor kontak, lalu data tersebut akan disimpan ke dalam sistem. Setelah itu, program dapat menampilkan daftar kontak yang telah tersimpan sehingga pengguna lebih mudah dalam melihat maupun mencari nomor kontak yang dibutuhkan. Sistem ini dibuat agar penyimpanan data kontak menjadi lebih rapi, teratur, dan mudah diakses.

Selain itu, program ini juga menggunakan konsep **BSD (Binary Search Data) lanjut** untuk mempercepat proses pencarian data kontak. Dengan metode tersebut, pengguna dapat menemukan kontak yang dicari dengan lebih efisien karena data diproses berdasarkan urutan tertentu.


<img width="430" height="192" alt="image" src="https://github.com/user-attachments/assets/d5707e75-1b86-4e4b-805c-a2d43def6ae8" />




Kode di atas digunakan untuk membuat sebuah class Node pada struktur data Binary Search Tree (BST). Pada bagian class Node:, program akan membuat sebuah template atau cetakan node yang nantinya bisa dipakai untuk menyimpan data. Lalu, def __init__(self, key): merupakan constructor yang otomatis akan berjalan saat object baru dibuat. Parameter key digunakan untuk menerima nilai atau data yang akan disimpan ke dalam node, sedangkan self digunakan untuk menghubungkan data tersebut ke object itu sendiri. Kemudian pada self.key = key, nilai yang dimasukkan akan disimpan sebagai data utama dari node.

Selanjutnya, self.left = None dan self.right = None digunakan untuk membuat cabang kiri dan kanan pada node dalam keadaan kosong terlebih dahulu. Pada Binary Search Tree, cabang kiri biasanya digunakan untuk menyimpan data yang nilainya lebih kecil, sedangkan cabang kanan digunakan untuk menyimpan data yang lebih besar dari node utama.





<img width="746" height="438" alt="image" src="https://github.com/user-attachments/assets/12a2e5b1-be0b-4761-8b43-75f604e6888c" />





Kode di atas berfungsi sebagai struktur utama dari Binary Search Tree (BST). Yang dimana, Pada bagian class BSTLanjut:, program akan membuat class baru untuk mengatur proses penyimpanan data pada tree. Kemudian, def __init__(self): adalah constructor yang akan berjalan otomatis saat object dibuat. Di dalamnya terdapat self.root = None yang berarti tree masih kosong dan belum memiliki data awal atau root. Root sendiri merupakan node utama atau node pertama dalam Binary Search Tree.

Selanjutnya, fungsi def insert_node(self, root, key): digunakan untuk menambahkan data baru ke dalam BST. Pada bagian if root is None:, program akan memeriksa apakah posisi node masih kosong. Jika kosong, maka program akan membuat node baru menggunakan return Node(key). Setelah itu, if key < root.key: digunakan untuk mengecek apakah data baru lebih kecil dari data root. Jika iya, maka data akan dimasukkan ke cabang kiri melalui root.left = self.insert_node(root.left, key). Sedangkan elif key > root.key: digunakan ketika data baru lebih besar dari root, sehingga data akan dimasukkan ke cabang kanan menggunakan root.right = self.insert_node(root.right, key). Terakhir, return root berfungsi untuk mengembalikan node root agar susunan nya tetap tersimpan dengan benar.




<img width="818" height="302" alt="image" src="https://github.com/user-attachments/assets/e7257d33-19e8-4d57-a593-77995cee000f" />










Kode `def insert(self, key):` digunakan untuk menambahkan data baru ke dalam BST dengan cara yang lebih sederhana. Pada bagian `self.root = self.insert_node(self.root, key)`, program akan memanggil fungsi `insert_node()` untuk memasukkan data baru sesuai aturan BST. Fungsi ini akan memeriksa apakah data harus ditempatkan di kiri atau kanan node. Lalu hasil akhirnya akan disimpan kembali ke `self.root` agar struktur tree tetap tersusun dengan benar. Dengan adanya fungsi ini, pengguna cukup memanggil `insert()` tanpa harus mengatur proses penempatan node secara manual. 

Selanjutnya, fungsi `def find_min_node(self, root):` digunakan untuk mencari nilai paling kecil dalam Binary Search Tree. Variabel `current = root` digunakan untuk menyimpan posisi awal pencarian. Lalu, pada bagian `while current is not None and current.left is not None:`, program akan terus bergerak ke node sebelah kiri selama masih ada cabang kiri. Hal ini karena pada BST, nilai terkecil selalu berada di posisi paling kiri. Setelah tidak ada lagi cabang kiri, program akan menghentikan perulangan dan `return current` akan mengembalikan node dengan nilai paling kecil tersebut.





<img width="915" height="571" alt="image" src="https://github.com/user-attachments/assets/a02b7d40-4280-42b1-b774-5830dc35cd31" />









Fungsi `def delete_node(self, root, key):` digunakan untuk menghapus data tertentu pada struktur Binary Search Tree (BST). Pada bagian `if root is None:`, program akan mengecek apakah node yang dicari ada atau tidak. Jika node kosong, maka fungsi akan mengembalikan `None`. Setelah itu, `if key < root.key:` digunakan untuk memeriksa apakah nilai yang ingin dihapus lebih kecil dari node saat ini, sehingga pencarian dilanjutkan ke cabang kiri melalui `root.left = self.delete_node(root.left, key)`. Sedangkan `elif key > root.key:` digunakan jika nilai yang dicari lebih besar, maka program akan melanjutkan pencarian ke cabang kanan menggunakan `root.right = self.delete_node(root.right, key)`.

Saat data berhasil ditemukan pada bagian `else:`, program akan menjalankan proses penghapusan node. Jika node tidak memiliki anak, yang ditunjukkan oleh `if root.left is None and root.right is None:`, maka node langsung dihapus dengan `return None`. Jika node hanya memiliki anak kanan, pada bagian `elif root.left is None:`, maka posisi node akan digantikan oleh anak kanannya menggunakan `return root.right`. Sebaliknya, jika node hanya mempunyai anak kiri, pada bagian `elif root.right is None:`, maka node akan diganti dengan anak kirinya melalui `return root.left`.

Namun, jika node memiliki dua anak, program akan mencari node pengganti dengan `successor = self.find_min_node(root.right)`. Node pengganti tersebut diambil dari nilai terkecil pada cabang kanan agar susunan BST tetap sesuai aturan. Setelah itu, nilai pada node lama akan diganti menggunakan `root.key = successor.key`. Kemudian, node pengganti yang sebelumnya dipakai akan dihapus kembali dengan `root.right = self.delete_node(root.right, successor.key)`. Di akhir fungsi, `return root` digunakan untuk mengembalikan struktur tree supaya tetap tersusun dengan baik setelah proses penghapusan dilakukan.









<img width="663" height="343" alt="image" src="https://github.com/user-attachments/assets/5502fd18-52a6-4a71-9138-88a1e0aed42d" />





Pada kode di atas, Pada baris awal yaitu `delete(self, key)` digunakan untuk menghapus data pada Binary Search Tree dengan bantuan fungsi `delete_node()`. Pada bagian `self.root = self.delete_node(self.root, key)`, program akan mencari data sesuai nilai `key`, lalu menghapusnya dan menyimpan kembali hasilnya ke root agar susunan tree tetap teratur.

Sementara itu, fungsi `height(self, root)` digunakan untuk mengetahui tinggi dari Binary Search Tree. Jika node kosong, maka program akan mengembalikan nilai `-1`. Setelah itu, program menghitung tinggi cabang kiri dan kanan menggunakan `height(root.left)` dan `height(root.right)`. Terakhir, `return 1 + max(height_left, height_right)` digunakan untuk menentukan tinggi tree dengan mengambil cabang yang paling tinggi kemudian ditambah 1.







<img width="548" height="496" alt="image" src="https://github.com/user-attachments/assets/2a5dba19-1a3a-4ea0-863f-e56b807f46ec" />





Pada baris pertama terdapat fungsi `level_order(self, root)` yang digunakan untuk menampilkan data pada Binary Search Tree (BST) secara berurutan berdasarkan level, dimulai dari root lalu dilanjutkan ke cabang kiri dan kanan. Pada bagian `if root is None:`, program akan memeriksa apakah tree kosong. Jika kosong, maka program akan menampilkan tulisan `"(kosong)"` lalu proses dihentikan menggunakan `return`.

Selanjutnya, program membuat list `queue = []` yang berfungsi sebagai antrian sementara untuk menyimpan node. Kemudian, `queue.append(root)` digunakan untuk memasukkan root ke dalam antrian. Pada bagian `while len(queue) > 0:`, program akan terus berjalan selama queue masih berisi data. Node pertama diambil menggunakan `current = queue.pop(0)` lalu nilainya ditampilkan dengan `print(current.key, end=" ")`. Setelah itu, jika node memiliki anak kiri atau kanan, maka node tersebut dimasukkan kembali ke dalam queue menggunakan `queue.append()`. Dengan cara ini, data pada BST dapat ditampilkan secara urut berdasarkan levelnya.






<img width="746" height="604" alt="image" src="https://github.com/user-attachments/assets/15775772-5230-490e-984d-47b476270107" />







Pada fungsi find_successor(self, root, key) digunakan untuk mencari nilai setelah suatu node atau disebut successor pada  BST. Variabel current = root digunakan untuk memulai pencarian dari root, sedangkan successor = None dipakai untuk menyimpan calon successor sementara. Pada bagian while current is not None:, program akan mencari node sesuai nilai key. Jika nilai key lebih kecil dari node saat ini, maka node tersebut dapat menjadi calon successor dan pencarian dilanjutkan ke cabang kiri. Jika lebih besar, pencarian akan diteruskan ke cabang kanan.

Setelah node ditemukan, program akan mengecek apakah node memiliki cabang kanan. Jika ada, maka successor dicari dari nilai terkecil pada cabang kanan menggunakan find_min_node(). Jika successor tidak ditemukan, fungsi akan mengembalikan None, False. Namun jika berhasil ditemukan, program akan mengembalikan nilai successor dengan return successor.key, True.














<img width="656" height="739" alt="image" src="https://github.com/user-attachments/assets/897531d1-dacd-4c9a-bf87-a2e8811cec33" />





Fungsi `find_predecessor()` dipakai untuk mencari nilai yang berada sebelum suatu node atau disebut **predecessor** pada Binary Search Tree (BST). Di awal fungsi, variabel `current = root` digunakan untuk memulai proses pencarian dari root, sedangkan `predecessor = None` berfungsi untuk menyimpan sementara node yang kemungkinan menjadi predecessor.

Pada bagian `while current is not None:`, program akan terus mencari node sesuai nilai `key`. Jika nilai `key` lebih besar dari node saat ini, maka node tersebut bisa menjadi calon predecessor sehingga disimpan ke variabel `predecessor`, lalu pencarian dilanjutkan ke cabang kanan. Sebaliknya, jika nilai `key` lebih kecil, maka pencarian diteruskan ke cabang kiri.

Setelah node ditemukan, program akan mengecek apakah node memiliki cabang kiri. Jika ada, maka predecessor dicari dari node dengan nilai terbesar pada cabang kiri dengan terus bergerak ke kanan. Jika predecessor berhasil ditemukan, program akan mengembalikan nilai tersebut. Namun jika predecessor tidak ada, maka fungsi akan mengembalikan `None`.



<img width="905" height="392" alt="image" src="https://github.com/user-attachments/assets/9c7b47ed-6d22-4de5-ae8c-65bfe0a165d7" />



Pada bagian `def main():`, program membuat fungsi utama untuk menjalankan sistem penyimpanan data nomor kontak. `bst = BSTLanjut()` digunakan untuk membuat object BST, sedangkan `pilih = 0` dipakai untuk menyimpan pilihan menu pengguna.

Bagian `while pilih != 7:` berfungsi untuk menampilkan menu secara berulang sampai pengguna memilih opsi keluar. Menu yang ditampilkan meliputi tambah kontak, hapus kontak, tampilkan data, melihat tinggi tree, mencari successor, predecessor, dan keluar dari program.



<img width="792" height="641" alt="image" src="https://github.com/user-attachments/assets/7feb1d24-ff29-4361-93f9-536f0b4ad69a" /> 








Pada bagian `try:` dan `except ValueError:`, program digunakan untuk memeriksa apakah input dari pengguna valid atau tidak. Jika pengguna memasukkan selain angka, maka program akan menampilkan pesan `"Input tidak valid!"` agar program tidak error. Nilai input pengguna kemudian disimpan ke variabel `pilih`.

Jika pengguna memilih menu `1`, program akan meminta pengguna memasukkan nomor kontak menggunakan `input()`. Setelah itu, data akan ditambahkan ke BST melalui `bst.insert(x)` dan program menampilkan pesan bahwa nomor kontak berhasil dimasukkan. Sedangkan pada pilihan `2`, program digunakan untuk menghapus nomor kontak dengan `bst.delete(x)` lalu menampilkan pesan bahwa data berhasil dihapus.

Pada pilihan `3`, program akan menampilkan seluruh data kontak yang tersimpan pada BST menggunakan fungsi `bst.level_order(bst.root)`. Data akan ditampilkan secara berurutan berdasarkan level pada tree.











<img width="893" height="743" alt="image" src="https://github.com/user-attachments/assets/f096fac8-c976-4aa5-8f9f-6f25ea01d142" />








Pada pilihan `4`, program digunakan untuk menampilkan tinggi dari Binary Search Tree melalui fungsi `bst.height(bst.root)`. Tinggi tree menunjukkan banyaknya level data kontak yang tersimpan di dalam sistem.

Pada pilihan `5`, pengguna dapat mencari **successor** atau nilai setelah suatu nomor kontak. Program akan meminta pengguna memasukkan nomor kontak, kemudian fungsi `find_successor()` akan mencari data tersebut. Jika successor ditemukan, hasilnya akan ditampilkan. Namun jika tidak ada, program akan menampilkan pesan `"Tidak ada successor"`.

Sementara itu, pada pilihan `6`, program dipakai untuk mencari **predecessor** atau nilai sebelum suatu nomor kontak dengan fungsi `find_predecessor()`. Jika predecessor ditemukan, maka hasilnya akan ditampilkan ke layar. Pada pilihan `7`, program akan dihentikan dan menampilkan pesan `"Program selesai."`. Sedangkan jika pengguna memasukkan pilihan yang tidak tersedia, program akan menampilkan pesan `"Pilihan tidak valid!"`.



<img width="391" height="124" alt="image" src="https://github.com/user-attachments/assets/506f435f-7782-4b68-8937-68704810efa1" />

