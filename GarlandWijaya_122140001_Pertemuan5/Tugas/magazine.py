from library_item import LibraryItem

class Magazine(LibraryItem):
    """
    Subclass dari LibraryItem yang merepresentasikan majalah.
    """

    def __init__(self, item_id: int, title: str, issue_number: int, is_available: bool = True):
        """
        Inisialisasi atribut spesifik untuk majalah.
        """
        super().__init__(item_id, title)
        self._issue_number = issue_number  # Protected attribute
        self._is_available = is_available  # Protected attribute

    @property
    def issue_number(self):
        """Getter untuk issue_number."""
        return self._issue_number

    @property
    def is_available(self):
        """Getter untuk is_available."""
        return self._is_available

    def display_info(self):
        """
        Menampilkan informasi tentang majalah.
        """
        availability = "Tersedia" if self.is_available else "Dipinjam"
        print(f"Majalah - ID: {self.item_id}, Judul: {self.title}, Nomor Edisi: {self.issue_number}, Status: {availability}")

    def check_availability(self):
        """
        Mengecek ketersediaan majalah.
        """
        return self._is_available

    def borrow(self):
        """
        Meminjam majalah jika tersedia.
        """
        if self.is_available:
            self._is_available = False
            print(f"Majalah '{self.title}' telah dipinjam.")
        else:
            print(f"Majalah '{self.title}' sedang dipinjam.")

    def return_magazine(self):
        """
        Mengembalikan majalah.
        """
        if not self.is_available:
            self._is_available = True
            print(f"Majalah '{self.title}' telah dikembalikan.")
        else:
            print(f"Majalah '{self.title}' sudah tersedia.")