class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' kitabı ödünç alındı.")
        else:
            print(f"'{self.title}' şu anda müsait değil.")

    def return_book(self):
        self.is_available = True
        print(f"'{self.title}' kitabı iade edildi.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' kütüphaneye eklendi.")

    def list_books(self):
        if not self.books:
            print("Kütüphanede kitap yok.")
            return

        for book in self.books:
            status = "Müsait" if book.is_available else "Ödünçte"
            print(f"{book.title} - {book.author} ({status})")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print("Kitap bulunamadı.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print("Kitap bulunamadı.")


# === UYGULAMA ===
library = Library()

book1 = Book("1984", "George Orwell")
book2 = Book("Suç ve Ceza", "Dostoyevski")

library.add_book(book1)
library.add_book(book2)

print("\nKütüphane Kitapları:")
library.list_books()

print("\nKitap Ödünç Alma:")
library.borrow_book("1984")

print("\nGüncel Durum:")
library.list_books()

print("\nKitap İade:")
library.return_book("1984")

print("\nSon Durum:")
library.list_books()
