import json
import os
from book import Book
from magazine import Magazine

class Library:
    def __init__(self):
        self._items = []
        self.data_file = 'data/items.json'
        self.load_from_file()

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        self._items.append(item)
        print(f"Item '{item.title}' telah ditambahkan ke perpustakaan.")
        self.save_to_file()

    def display_all_items(self):
        if not self._items:
            print("Tidak ada item di perpustakaan.")
            return
        print("Daftar Item Perpustakaan:")
        for item in self._items:
            item.display_info()

    def search_by_title(self, title):
        found_items = [item for item in self._items if title.lower() in item.title.lower()]
        if found_items:
            print(f"Hasil pencarian untuk judul '{title}':")
            for item in found_items:
                item.display_info()
        else:
            print(f"Tidak ditemukan item dengan judul '{title}'.")

    def search_by_id(self, item_id):
        for item in self._items:
            if item.item_id == item_id:
                print(f"Item dengan ID {item_id}:")
                item.display_info()
                return
        print(f"Tidak ditemukan item dengan ID {item_id}.")

    def borrow_items_by_ids(self, ids: list):
        for item_id in ids:
            found = False
            for item in self._items:
                if item.item_id == item_id:
                    found = True
                    if isinstance(item, Book) or isinstance(item, Magazine):
                        item.borrow()
                    break
            if not found:
                print(f"Tidak ditemukan item dengan ID {item_id}.")
        self.save_to_file()

    def remove_item_by_id(self, item_id):
        for i, item in enumerate(self._items):
            if item.item_id == item_id:
                if isinstance(item, Book) or isinstance(item, Magazine):
                    if not item.is_available:
                        print(f"Item '{item.title}' berhasil dihapus karena sedang dipinjam.")
                        del self._items[i]
                        self.save_to_file()
                        return
                    else:
                        print(f"Item '{item.title}' tidak dapat dihapus karena masih tersedia.")
                        return
        print(f"Tidak ditemukan item dengan ID {item_id} atau item tidak memenuhi syarat untuk dihapus.")

    def save_to_file(self):
        """Menyimpan semua item ke file JSON"""
        data = []
        for item in self._items:
            if isinstance(item, Book):
                data.append({
                    "type": "Book",
                    "item_id": item.item_id,
                    "title": item.title,
                    "author": item.author,
                    "is_available": item.is_available
                })
            elif isinstance(item, Magazine):
                data.append({
                    "type": "Magazine",
                    "item_id": item.item_id,
                    "title": item.title,
                    "issue_number": item.issue_number,
                    "is_available": item.is_available
                })

        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        """Memuat item dari file JSON jika file tersedia"""
        if not os.path.exists(self.data_file):
            print("⚠️ File data tidak ditemukan. Memulai dengan daftar kosong.")
            return

        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for item_data in data:
                    if item_data["type"] == "Book":
                        book = Book(
                            item_id=item_data["item_id"],
                            title=item_data["title"],
                            author=item_data["author"],
                            is_available=item_data["is_available"]
                        )
                        self._items.append(book)
                    elif item_data["type"] == "Magazine":
                        magazine = Magazine(
                            item_id=item_data["item_id"],
                            title=item_data["title"],
                            issue_number=item_data["issue_number"],
                            is_available=item_data["is_available"]
                        )
                        self._items.append(magazine)
                print(f"✅ Berhasil memuat {len(data)} item dari file.")
        except Exception as e:
            print(f"❌ Gagal memuat file: {e}")