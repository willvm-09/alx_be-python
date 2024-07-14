class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []
        

    def add_book(self, title, author):
        book = Book(title, author)
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print (f"{title} has been checked out.")
                else:
                    print(f"{title} not found in library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"{title} has been returned.")
                else:
                    print(f"{title} is not currently checked out.")
                return print(f"{title} not found in the library.")
    
    def list_available_books(self):
        available_books = [book.title for bok in self._books if book.is_available()]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(book)
        else:
            print("No books available.")
