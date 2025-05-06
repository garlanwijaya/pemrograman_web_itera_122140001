from library import Library
from book import Book
from magazine import Magazine

def tampilkan_menu():
    print("\n📚 SELAMAT DATANG DI PERPUSTAKAAN 📚")
    print("======================================")
    print("1. Melihat semua daftar buku dan majalah")
    print("2. Melihat daftar buku yang tersedia")
    print("3. Melihat daftar majalah yang tersedia")
    print("4. Meminjam buku/majalah")
    print("5. Mengembalikan buku/majalah")
    print("6. Keluar dari program")
    print("======================================")

def main():
    library = Library()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            print("\n📋 Daftar Semua Item Perpustakaan:")
            library.display_all_items()

        elif pilihan == '2':
            print("\n📘 Daftar Buku Yang Tersedia:")
            available_books = [item for item in library.items if isinstance(item, Book) and item.is_available]
            if available_books:
                for book in available_books:
                    book.display_info()
            else:
                print("Tidak ada buku yang tersedia.")

        elif pilihan == '3':
            print("\n🗞️ Daftar Majalah Yang Tersedia:")
            available_magazines = [item for item in library.items if isinstance(item, Magazine) and item.is_available]
            if available_magazines:
                for magazine in available_magazines:
                    magazine.display_info()
            else:
                print("Tidak ada majalah yang tersedia.")

        elif pilihan == '4':
            print("\n🔍 Peminjaman Buku/Majalah")
            metode = input("Cari berdasarkan (1) Judul / (2) ID ? ")
            if metode == '1':
                title = input("Masukkan judul: ")
                library.search_by_title(title)
                try:
                    item_id = int(input("Masukkan ID item yang ingin dipinjam: "))
                    library.borrow_items_by_ids([item_id])
                except ValueError:
                    print("ID harus berupa angka.")
            elif metode == '2':
                try:
                    item_id = int(input("Masukkan ID item: "))
                    library.borrow_items_by_ids([item_id])
                except ValueError:
                    print("ID harus berupa angka.")
            else:
                print("Metode pencarian tidak valid.")

        elif pilihan == '5':
            print("\n📦 Pengembalian Buku/Majalah")
            try:
                item_id = int(input("Masukkan ID item yang dikembalikan: "))
                found = False
                for item in library.items:
                    if item.item_id == item_id:
                        found = True
                        if not item.is_available:
                            if isinstance(item, Book):
                                item.return_book()
                            elif isinstance(item, Magazine):
                                item.return_magazine()
                        else:
                            print(f"Item '{item.title}' tidak sedang dipinjam.")
                        library.save_to_file()
                        break
                if not found:
                    print(f"Tidak ditemukan item dengan ID {item_id}.")
            except ValueError:
                print("ID harus berupa angka.")

        elif pilihan == '6':
            print("\n👋 Terima kasih telah berkunjung, silahkan datang kembali.")
            break

        else:
            print("\n❌ Pilihan tidak valid. Silakan coba lagi.")
    
if __name__ == "__main__": 
    main()