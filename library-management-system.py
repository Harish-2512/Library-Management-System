class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Not Available'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"You have borrowed '{book.title}'.")
                else:
                    print(f"Sorry, '{book.title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"You have returned '{book.title}'.")
                else:
                    print(f"'{book.title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                return
        print(f"No books found with title containing '{title}'.")


# Example usage
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Search for a book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            library.borrow_book(title)
        elif choice == '4':
            title = input("Enter the title of the book to return: ")
            library.return_book(title)
        elif choice == '5':
            title = input("Enter the title to search: ")
            library.search_book(title)
        elif choice == '6':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
