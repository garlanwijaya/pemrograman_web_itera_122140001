# Deskripsi Aplikasi  
Aplikasi yang saya buat ini adalah sebuah website daftar buku-buku yang mempunyai 3 kategori yaitu:  
- Dimiliki  
- Sedang Dibaca
- Ingin Dibeli
  
Aplikasi saya mempunya 3 fitur, yaitu user dapat menambah daftar buku yang ingin dibuatkan list dan memilih diantara 3 kategori diatas. kedua, user dapat mencari buku berdasarkan nama / judul dari buku nya menggunakan fitur searching. User juga dapat sortir buku berdasarkan 3 Kategori diatas yang menampilkan kategori apa yang dipilih. selain itu, pengguna dapat menghapus buku yang berada di dalam ListBook.

Aplikasi ini juga dibuat menggunakan LocalStorage untuk penyimpanan Data ListBook, sehingga user tidak perlu takut ketika halaman ter load ulang. Aplikasi ini juga sudah responsive dan dapat dibuka lewat mobile / IOS.  

# Instruksi Instalasi dan Menjalankan  
saat tahap pengembangan, saya menginstalasi beberapa module seperti:  
- Node module untuk menginstalasi hal-hal yang diperlukan oleh suatu kerangka kerja jika ingin menggunakan library tertentu.
- React-Router-Dom ini berfungsi agar kita dapat memindah halaman lain, namun pada kasus aplikasi saya, module ini berfungsi agar 1 fungsi dan fungsi lainnya dapat bekerja secara independen.
- Jest yang berfungsi sebagai perintah testing untuk menguji suatu fungsi yang telah saya buat.

# Screenshot antarmuka  
![image](https://github.com/user-attachments/assets/9c737f29-edb7-41b5-bda6-5b18aeb1d708)  
  
# Penjelasan fitur React yang digunakan  
## Components  
- BookList -> daftar list buku yang telah diinput oleh user
- BookForm -> form untuk list buku yang ingin ditambahkan ke dalam localStorage dan di tampilkan di web
- BookFilter -> fitur filterisasi buku berdasarkan kategori.
## Context  
- tempat menambahkan Fungsi seperti addBook + updateBook + deleteBook
## Hooks  
- useBookStats -> memberi label pada buku (Dimiliki, Sedang dibaca, dan Ingin dibeli)
- useLocalStorage -> menginput data yang telah user input ke dalam localStorage.
## Pages  
- Home -> untuk menampilkan Managemen Buku
- Stats -> untuk menampilkan status dari buku (total buku, jumlah buku di kategori tertentu).
# Laporan Testing  
![image](https://github.com/user-attachments/assets/fcf4acb2-db4f-43fc-b0d1-5989df9414c6)
