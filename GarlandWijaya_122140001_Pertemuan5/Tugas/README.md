# 📚 Aplikasi Perpustakaan Berbasis OOP  
Aplikasi ini merupakan sistem manajemen perpustakaan sederhana menggunakan konsep Object-Oriented Programming (OOP)   dalam Python. Program menyediakan dua versi:  
  
✅ CLI (Command Line Interface) – Cocok untuk pengguna biasa dan admin  
✅ GUI (Tkinter) – Antarmuka visual dengan login role (User/Admin)  
Data item seperti buku dan majalah disimpan secara permanen dalam file JSON.  
  
# 🗂️ Struktur Proyek  
  
library_project/  
│  
├── library_item.py       ← Abstract class dasar LibraryItem  
├── book.py               ← Class Buku  
├── magazine.py           ← Class Majalah  
├── library.py            ← Logika utama perpustakaan  
├── main.py               ← Versi CLI  
├── main_gui.py           ← Versi GUI dengan Tkinter  
│  
├── data/  
│   ├── items.json        ← Daftar buku/majalah  
│   └── users.json        ← Data user/admin  
│  
└── README.md             ← Dokumentasi ini  
  
# 🧰 Fitur Utama  

  
# 🖥️ Cara Menjalankan Program  
1. Jalankan Versi CLI (main.py)  
💡 Fungsi:  
Untuk pengguna biasa  
Semua fitur kecuali tambah/hapus item  
  
▶️ Langkah-langkah:  

  
Program akan menampilkan menu interaktif untuk:  
  
- Melihat daftar item  
- Meminjam dan mengembalikan item  
  
2. Jalankan Versi GUI (main_gui.py)  
💡 Fungsi:  
Antarmuka visual  
Login role (User/Admin)  
Semua fitur sesuai role  
  
▶️ Langkah-langkah:  

  
Program akan membuka jendela login:  
  
Masukkan username dan password:  
User: user / user123  
Admin: admin / admin123  
Setelah login, tampilan akan berbeda tergantung role:  
  
User : hanya bisa lihat, pinjam, kembalikan  
Admin : bisa tambah & hapus item juga  
  
# ⚙️ Persyaratan Sistem  
Python 3.x  
Modul bawaan: tkinter, abc, json, os  
Tidak ada dependensi eksternal  
  
# 🛠️ Penjelasan Teknis  
Konsep Pemrograman yang Digunakan  
Class & Object – Setiap item didefinisikan sebagai objek.  
Inheritance – Book dan Magazine mewarisi dari LibraryItem.  
Encapsulation – Data dilindungi dengan access modifier.  
Polymorphism – Method seperti display_info() memiliki implementasi berbeda di tiap subclass.  
File Persistence – Data tersimpan di file JSON agar tetap ada meskipun program ditutup.  
  
# 📌 Catatan Penting  
Pastikan folder data/ dan file items.json, users.json sudah dibuat sebelum menjalankan program.  
Jika file tidak ditemukan, program akan memulai dengan daftar kosong.  
Gunakan mode Admin untuk menambahkan item pertama kali.  
  
# 📦 Contoh Output CLI  
  
📚 SELAMAT DATANG DI PERPUSTAKAAN 📚  
======================================  
1. Melihat semua daftar buku dan majalah  
2. Melihat daftar buku yang tersedia  
3. Melihat daftar majalah yang tersedia  
4. Meminjam buku/majalah  
5. Mengembalikan buku/majalah  
6. Keluar dari program  
======================================
Pilih menu (1-6): 2  
  
# 📝 Kesimpulan
Program ini adalah contoh implementasi OOP dalam Python yang mudah dipelajari dan dikembangkan lebih lanjut. Cocok digunakan untuk pembelajaran atau dikembangkan menjadi aplikasi nyata.  