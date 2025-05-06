from abc import ABC, abstractmethod

class LibraryItem(ABC):
    """
    Abstract class yang menjadi dasar untuk semua item di perpustakaan.
    """

    def __init__(self, item_id: int, title: str):
        """
        Inisialisasi atribut umum untuk setiap item perpustakaan.
        """
        self._item_id = item_id  # Protected attribute
        self._title = title      # Protected attribute

    @property
    def item_id(self):
        """Getter untuk item_id."""
        return self._item_id

    @property
    def title(self):
        """Getter untuk title."""
        return self._title

    @abstractmethod
    def display_info(self):
        """
        Method abstrak yang harus diimplementasikan oleh subclass.
        """
        pass

    @abstractmethod
    def check_availability(self):
        """
        Method abstrak untuk mengecek ketersediaan item.
        """
        pass