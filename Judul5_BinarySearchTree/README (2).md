PROGRAM ANTRIAN MENGAMBIL MAKANAN BERGIZI GRATIS (MBG)




Program Antrian Pengambilan Makanan Bergizi Gratis (MBG) adalah sebuah program yang vdibuat untuk membantu mengatur proses antrean dalam pembagian makanan bergizi gratis agar berjalan dengan tertib dan terorganisir.
Melalui program ini, petugas dapat menambahkan data peserta antrean, melihat daftar antrean yang sedang menunggu, serta menghapus antrean yang sudah mendapatkan makanan. Dengan sistem ini, proses pembagian makanan menjadi lebih mudah, efisien, dan tidak menimbulkan kerumunan yang tidak teratur.


Pada program ini digunakan struktur data Queue (Antrian) dengan metode FIFO (First In First Out). Konsep tersebut berarti orang yang pertama masuk ke antrean akan menjadi orang pertama yang dilayani. Struktur data queue dipilih karena sesuai dengan mekanisme antrean dalam kehidupan sehari-hari, seperti antrean saat mengambil makanan, membeli tiket, ataupun pelayanan umum lainnya.


<img width="476" height="193" alt="image" src="https://github.com/user-attachments/assets/8c3d8fa2-8298-4610-b03b-69b4125e7e52" />

Pada baris pertama yaitu, class QueueArray: yang digunakan untuk membuat sebuah class bernama QueueArray yang dipakai sebagai sistem antrian dengan metode queue berbasis array. Pada bagian def __init__(self, max_size=100):, terdapat constructor yang akan berjalan secara otomatis saat object dibuat. Parameter max_size=100 menandakan bahwa jumlah maksimal data yang dapat ditampung di dalam antrian adalah 100 data. Lalu, kode self.MAXN = max_size berfungsi untuk menyimpan kapasitas maksimum antrian ke dalam variabel MAXN.



Berikutnya, pada kode self.q = [None] * self.MAXN digunakan untuk membuat sebuah array kosong sesuai jumlah kapasitas yang sudah ditentukan sebelumnya. Isi awal array berupa None, yang berarti belum ada data yang tersimpan. Kemudian, kode self.front_idx = -1 dipakai untuk menunjukkan posisi depan antrian, sedangkan self.rear_idx = -1 digunakan untuk menunjukkan posisi belakang antrian. Nilai awal -1 pada kedua variabel tersebut menandakan bahwa kondisi antrian masih kosong atau belum berisi data sama sekali.

<img width="743" height="158" alt="image" src="https://github.com/user-attachments/assets/2b838f12-609c-425d-92bf-ae13de862c31" />

Pada baris ke 8, Kode ini "def is_empty(self):" berfungsi untuk mengecek kondisi apakah antrian sedang kosong atau tidak. Pada bagian return self.front_idx == -1, program akan memberikan nilai True apabila variabel front_idx bernilai -1. Nilai tersebut menunjukkan bahwa belum ada data yang tersimpan di dalam antrian. Sebaliknya, jika nilainya tidak -1, maka fungsi akan menghasilkan False, yang berarti antrian sudah terisi data.

Sementara itu, kode def is_full(self): digunakan untuk mengetahui apakah kapasitas antrian sudah penuh. Pada bagian return (self.rear_idx + 1) % self.MAXN == self.front_idx, program melakukan pengecekan menggunakan konsep circular queue atau antrian melingkar. Jika posisi belakang antrian setelah ditambah satu sama dengan posisi depan antrian, maka antrian dinyatakan penuh dan fungsi akan menghasilkan nilai True. Namun jika tidak sama, maka fungsi akan menghasilkan False, yang berarti masih tersedia tempat kosong pada antrian.


<img width="773" height="372" alt="image" src="https://github.com/user-attachments/assets/319cbb9e-8f8c-49ca-8341-e8c3e50d142d" />

Pada bais ini, Kode def enqueue(self, x): digunakan untuk menambahkan data baru ke dalam antrian. Parameter x merupakan data yang akan dimasukkan, seperti nama atau nomor antrean peserta MBG. Pada bagian if self.is_full():, program akan memeriksa terlebih dahulu apakah kapasitas antrian sudah penuh atau belum. Jika antrian sudah penuh, maka program menampilkan pesan "Antrian MBG penuh" dan proses penambahan data langsung dihentikan menggunakan return.

selanjutnya, ada kode if self.is_empty(): digunakan untuk mengecek apakah antrian masih kosong. Jika kosong, maka nilai front_idx dan rear_idx diubah menjadi 0 sebagai tanda bahwa data pertama telah masuk ke antrian. Namun jika antrian sudah terisi, maka posisi belakang antrian akan berpindah ke indeks berikutnya menggunakan konsep circular queue pada kode self.rear_idx = (self.rear_idx + 1) % self.MAXN. Setelah itu, data disimpan ke dalam array melalui kode self.q[self.rear_idx] = x, lalu program akan menampilkan pesan bahwa data berhasil ditambahkan ke dalam antrian.


<img width="998" height="381" alt="image" src="https://github.com/user-attachments/assets/673392cd-6966-4d42-9ffb-e36682b11ffc" />

Kode `def dequeue(self):` berfungsi untuk menghapus atau mengambil elemen dari bagian awal antrian. Pada baris `if self. is_empty():`, program terlebih dahulu memeriksa apakah antrian dalam keadaan kosong. Bila antrian tidak memiliki elemen, maka program akan menampilkan pesan `"Antrian MBG kosong"` dan proses pengambilan data akan dihentikan dengan menggunakan `return`. Namun jika antrian masih menyimpan elemen, program akan menunjukkan pesan bahwa elemen pada posisi paling depan berhasil mengambil makanan bergizi tanpa biaya.

Selanjutnya, pernyataan `if self. front_idx == self. rear_idx:` digunakan untuk mengecek apakah elemen yang diambil adalah elemen terakhir dalam antrian. Jika ya, maka nilai `front_idx` dan `rear_idx` akan direset menjadi `-1`, menandakan bahwa antrian kini kembali kosong. Namun, jika masih tersisa elemen lain dalam antrian, maka posisi depan antrian akan dipindahkan ke indeks berikutnya melalui konsep antrian melingkar yang dituliskan dalam kode `self. front_idx = (self. front_idx + 1) % self. MAXN`.




<img width="753" height="397" alt="Screenshot 2026-05-18 144621" src="https://github.com/user-attachments/assets/84c7d0fd-90f2-4cac-819f-b635c31db6c0" />



Kode `def peek(self):` digunakan untuk memeriksa nilai yang terdapat di awal antrian tanpa menghapusnya dari struktur data. Pada bagian `if self. is_empty():`, sistem akan mengevaluasi apakah antrian dalam keadaan kosong. Apabila iya, maka program akan menampilkan pesan `"Antrian MBG kosong"` dan menghentikan proses dengan menggunakan `return`. Namun jika antrian berisi elemen, maka program akan menampilkan nilai yang ada di bagian depan antrian melalui kode `print(f"Antrian depan: {self. q[self. front_idx]}")`.

Sementara itu, kode `def display(self):` memiliki tujuan untuk menampilkan semua elemen dalam antrian dari depan hingga belakang. Sama seperti proses sebelumnya, program akan memeriksa terlebih dahulu apakah antrian kosong menggunakan `if self. is_empty():`. Jika antrian kosong, maka akan ditampilkan pesan `"Antrian MBG kosong"`. Namun jika ada data dalam antrian, maka program akan menunjukkan tulisan `"Isi antrian MBG (depan ke belakang):"` sebagai indikasi bahwa semua elemen antrian akan ditampilkan dalam urutan dari depan ke belakang.


<img width="439" height="318" alt="image" src="https://github.com/user-attachments/assets/cb93cba3-216a-4e93-98b4-d58102df3188" />


Kode `i = self. front_idx` berfungsi untuk menyimpan lokasi depan antrian ke dalam variabel `i`. Variabel ini kemudian digunakan sebagai referensi untuk menampilkan semua elemen dalam antrian. Selanjutnya, di bagian `while True:`, program melakukan loop tanpa akhir untuk menampilkan data antrian satu per satu mulai dari posisi terdepan.

Pada baris kode `print(self. q[i], end=" ")`, program menunjukkan data yang ada di indeks `i` tanpa berpindah ke baris baru. Selanjutnya, bagian `if i == self. rear_idx:` berfungsi untuk mengecek apakah posisi yang sedang ditampilkan telah mencapai bagian belakang antrian. Jika sudah, perulangan akan dihentikan dengan perintah `break`. Namun jika masih belum sampai di bagian belakang antrian, maka kode `i = (i + 1) % self. MAXN` akan mengubah indeks ke posisi berikutnya dengan menggunakan konsep antrian melingkar. Di akhir, kode `print()` digunakan untuk membuat baris baru setelah semua isi antrian selesai ditampilkan.




<img width="714" height="349" alt="image" src="https://github.com/user-attachments/assets/e4fa2c8c-9aaf-43f6-9caa-e9dafeaf063c" />


Fungsi `def main():` berperan sebagai inti untuk menjalankan program sistem antrian MBG. Pada baris `queue = QueueArray()`, program menciptakan objek baru dari kelas `QueueArray` yang akan digunakan untuk mengelola semua tahapan antrian. Selanjutnya, kode `pilih = 0` berfungsi untuk menyimpan pilihan yang dibuat oleh pengguna. Nilai awal ditetapkan ke `0` supaya siklus program dapat dimulai untuk pertama kalinya.

Setelah itu, kode `while pilih ! = 5:` digunakan untuk menjalankan menu secara berkesinambungan hingga pengguna memilih opsi `5` yang berarti keluar dari program. Dalam siklus tersebut, program mempresentasikan beberapa pilihan menu melalui `print()`, yang mencakup opsi untuk menambah antrian, mengambil makanan, melihat antrian terdepan, menampilkan isi antrian, dan keluar dari aplikasi. Dengan adanya pilihan menu ini, pengguna dapat menjalankan program antrian MBG dengan cara yang lebih praktis dan terorganisir.


<img width="550" height="629" alt="image" src="https://github.com/user-attachments/assets/9b012c48-64bc-4212-91ea-14ba93916a3f" />


Kode `try:` digunakan untuk menangani kemungkinan kesalahan saat pengguna memasukkan pilihan menu. Pada bagian `pilih = int(input("Pilih: "))`, program meminta pengguna memasukkan angka sesuai menu yang tersedia. Jika pengguna memasukkan data selain angka, maka program akan masuk ke bagian `except ValueError:` dan menampilkan pesan `"Input tidak valid!"`. Setelah itu, kode `continue` digunakan agar program kembali menampilkan menu tanpa berhenti.

Selanjutnya, kode `if pilih == 1:` digunakan ketika pengguna memilih menu tambah antrian. Program akan meminta input nilai lalu menjalankan fungsi `queue.enqueue(val)` untuk menambahkan data ke antrian. Pada bagian `elif pilih == 2:`, program menjalankan fungsi `queue.dequeue()` untuk mengambil antrian. Kode `elif pilih == 3:` digunakan untuk melihat antrian paling depan dengan fungsi `queue.peek()`, sedangkan `elif pilih == 4:` digunakan untuk menampilkan seluruh isi antrian melalui fungsi `queue.display()`. Jika pengguna memilih `5`, maka program akan menampilkan pesan `"Program selesai."` dan berhenti. Namun jika pilihan menu tidak sesuai, program akan menampilkan pesan `"Pilihan tidak valid!"`.



<img width="503" height="197" alt="image" src="https://github.com/user-attachments/assets/e5547119-d658-4526-9653-151c2fbd7eb1" />




Kode `if __name__ == "__main__":` digunakan untuk mengecek apakah file Python sedang dijalankan secara langsung atau tidak. Kondisi ini dibuat agar program utama hanya berjalan saat file tersebut dieksekusi sendiri, bukan ketika dipanggil dari file Python lain.

Sedangkan kode `main()` berfungsi untuk memanggil fungsi utama yang berisi seluruh proses program antrian MBG. Dengan adanya pemanggilan fungsi ini, program dapat langsung menjalankan menu dan semua fitur antrian saat program dijalankan.



<img width="428" height="783" alt="image" src="https://github.com/user-attachments/assets/5fdc515a-6191-482a-a838-24993e552e82" />

<img width="970" height="793" alt="image" src="https://github.com/user-attachments/assets/66a8e88b-dddb-47fb-9d5c-d4ea2471214a" />

Pada output di awal, Pengunna akan diberi 5 pilihan, Yaitu ada tambah antrian, ambil makanan, lihat antrian di depan, tampilan, dan keluar. Lalu pengguna memilih no 1, Yang dimana pengguna harus memasukan angka yang ingin di masukan sampai yang di ingin kan. Lalu pengguna memilih menu 4 (Tampilkan) sehingga program menampilkan isi antrian MBG dari depan ke belakang, yaitu 2 2 4 3 5 7. Angka-angka tersebut merupakan data yang sudah dimasukkan sebelumnya ke dalam antrian. Setelah itu, pengguna memilih menu 2 (Ambil Makanan) sehingga program menjalankan proses dequeue, yaitu menghapus data paling depan dari antrian. Karena data terdepan adalah angka 2, maka program menampilkan pesan 2 berhasil mengambil makanan bergizi gratis yang menandakan bahwa data tersebut sudah keluar dari antrian.

Selanjutnya, pengguna memilih menu 3 (Lihat Antrian Depan) untuk melihat data yang sekarang berada di posisi paling depan. Program menampilkan Antrian depan: 2, yang berarti masih ada angka 2 lain di urutan depan antrian. Setelah itu, saat pengguna kembali memilih menu 4 (Tampilkan), program menampilkan isi antrian terbaru yaitu 2 4 3 5 7. Hal ini menunjukkan bahwa angka 2 yang pertama sudah berhasil dihapus dari antrian setelah proses pengambilan makanan dilakukan.
