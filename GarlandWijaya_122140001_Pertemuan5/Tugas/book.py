from library_item import LibraryItem

class Book(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan buku.
    """

    def __init__(self, item_id: int, title: str, author: str, is_available: bool = True):
        """
        Inisialisasi atribut spesifik untuk buku.
        """
        super().__init__(item_id, title)
        self._author = author  # Protected attribute
        self._is_available = is_available  # Protected attribute

    @property
    def author(self):
        """Getter untuk author."""
        return self._author

    @property
    def is_available(self):
        """Getter untuk is_available."""
        return self._is_available

    def display_info(self):
        """
        Menampilkan informasi tentang buku.
        """
        availability = "Tersedia" if self.is_available else "Dipinjam"
        print(f"Buku - ID: {self.item_id}, Judul: {self.title}, Penulis: {self.author}, Status: {availability}")

    def check_availability(self):
        """
        Mengecek ketersediaan buku.
        """
        return self._is_available

    def borrow(self):
        """
        Meminjam buku jika tersedia.
        """
        if self.is_available:
            self._is_available = False
            print(f"Buku '{self.title}' telah dipinjam.")
        else:
            print(f"Buku '{self.title}' sedang dipinjam.")

    def return_book(self):
        """
        Mengembalikan buku.
        """
        if not self.is_available:
            self._is_available = True
            print(f"Buku '{self.title}' telah dikembalikan.")
        else:
            print(f"Buku '{self.title}' sudah tersedia.")