# main_gui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from library import Library
from book import Book
from magazine import Magazine


class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success

        self.login_window = tk.Toplevel(root)
        self.login_window.title("🔐 Login")
        self.login_window.geometry("300x150")
        self.login_window.resizable(False, False)

        self.username_label = tk.Label(self.login_window, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.login_window)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_window, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_window, text="Login", command=self.check_login)
        self.login_button.pack(pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        users_file = 'data/users.json'

        if not os.path.exists(users_file):
            messagebox.showerror("Error", "File pengguna tidak ditemukan.")
            return

        with open(users_file, 'r') as f:
            users = json.load(f)

        for user in users:
            if user['username'] == username and user['password'] == password:
                self.login_window.destroy()
                self.on_login_success(user['role'])
                return

        messagebox.showerror("Error", "Username atau password salah.")


class LibraryApp:
    def __init__(self, root, role):
        self.library = Library()
        self.root = root
        self.role = role
        self.root.title("📚 Aplikasi Perpustakaan")
        self.root.geometry("600x400")

        # Tombol Menu sesuai role
        self.btn_frame = tk.Frame(self.root)
        self.btn_frame.pack(pady=10)

        self.btn_all = tk.Button(self.btn_frame, text="Lihat Semua Item", width=20, command=self.show_all_items)
        self.btn_all.grid(row=0, column=0, padx=5)

        self.btn_books = tk.Button(self.btn_frame, text="Buku Tersedia", width=20, command=self.show_available_books)
        self.btn_books.grid(row=0, column=1, padx=5)

        self.btn_magazines = tk.Button(self.btn_frame, text="Majalah Tersedia", width=20, command=self.show_available_magazines)
        self.btn_magazines.grid(row=0, column=2, padx=5)

        self.btn_borrow = tk.Button(self.root, text="Pinjam Buku/Majalah", width=30, command=self.borrow_item)
        self.btn_borrow.pack(pady=10)

        self.btn_return = tk.Button(self.root, text="Kembalikan Buku/Majalah", width=30, command=self.return_item)
        self.btn_return.pack(pady=10)

        # Admin-only buttons
        if role == "admin":
            self.btn_add = tk.Button(self.root, text="Tambah Buku/Majalah", width=30, command=self.add_item)
            self.btn_add.pack(pady=5)

            self.btn_remove = tk.Button(self.root, text="Hapus Buku/Majalah", width=30, command=self.remove_item)
            self.btn_remove.pack(pady=5)

        self.btnExit = tk.Button(self.root, text="Keluar", width=30, command=self.exit_app)
        self.btnExit.pack(pady=10)

        # Area Output
        self.output_text = tk.Text(self.root, height=10, width=70, state='disabled')
        self.output_text.pack(pady=10)

    def display_items(self, items):
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        if not items:
            self.output_text.insert(tk.END, "Tidak ada item.\n")
        else:
            for item in items:
                status = "Tersedia" if item.is_available else "Dipinjam"
                if hasattr(item, 'author'):
                    line = f"[Buku] ID: {item.item_id}, Judul: {item.title}, Penulis: {item.author}, Status: {status}\n"
                elif hasattr(item, 'issue_number'):
                    line = f"[Majalah] ID: {item.item_id}, Judul: {item.title}, Edisi: {item.issue_number}, Status: {status}\n"
                else:
                    line = f"[Item] ID: {item.item_id}, Judul: {item.title}, Status: {status}\n"
                self.output_text.insert(tk.END, line)
        self.output_text.config(state='disabled')

    def show_all_items(self):
        self.display_items(self.library.items)

    def show_available_books(self):
        books = [item for item in self.library.items if hasattr(item, 'author') and item.is_available]
        self.display_items(books)

    def show_available_magazines(self):
        mags = [item for item in self.library.items if hasattr(item, 'issue_number') and item.is_available]
        self.display_items(mags)

    def borrow_item(self):
        try:
            item_id = int(simpledialog.askstring("Input", "Masukkan ID item yang ingin dipinjam:"))
            self.library.borrow_items_by_ids([item_id])
            self.show_all_items()
        except (TypeError, ValueError):
            messagebox.showerror("Error", "ID harus berupa angka.")

    def return_item(self):
        try:
            item_id = int(simpledialog.askstring("Input", "Masukkan ID item yang dikembalikan:"))
            found = False
            for item in self.library.items:
                if item.item_id == item_id:
                    found = True
                    if not item.is_available:
                        if hasattr(item, 'author'):
                            item.return_book()
                        elif hasattr(item, 'issue_number'):
                            item.return_magazine()
                        self.library.save_to_file()
                        messagebox.showinfo("Info", f"{item.title} berhasil dikembalikan.")
                    else:
                        messagebox.showwarning("Peringatan", f"{item.title} tidak sedang dipinjam.")
                    break
            if not found:
                messagebox.showerror("Error", f"Tidak ditemukan item dengan ID {item_id}.")
            self.show_all_items()
        except (TypeError, ValueError):
            messagebox.showerror("Error", "ID harus berupa angka.")

    def add_item(self):
        jenis = simpledialog.askstring("Input", "Jenis item (buku/majalah)?")
        if jenis.lower() not in ['buku', 'majalah']:
            messagebox.showerror("Error", "Jenis item tidak valid.")
            return

        try:
            item_id = int(simpledialog.askstring("Input", "Masukkan ID item: "))
            title = simpledialog.askstring("Input", "Judul item:")

            if jenis.lower() == 'buku':
                author = simpledialog.askstring("Input", "Penulis:")
                self.library.add_item(Book(item_id=item_id, title=title, author=author))
            elif jenis.lower() == 'majalah':
                issue_number = int(simpledialog.askstring("Input", "Nomor edisi:"))
                self.library.add_item(Magazine(item_id=item_id, title=title, issue_number=issue_number))

            self.show_all_items()
        except Exception as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    def remove_item(self):
        try:
            item_id = int(simpledialog.askstring("Input", "Masukkan ID item yang ingin dihapus (harus dipinjam):"))
            self.library.remove_item_by_id(item_id)
            self.show_all_items()
        except (TypeError, ValueError):
            messagebox.showerror("Error", "ID harus berupa angka.")

    def exit_app(self):
        self.root.destroy()


def run_app(role):
    root = tk.Tk()
    app = LibraryApp(root, role)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide main window until login
    LoginWindow(root, run_app)
    root.mainloop()