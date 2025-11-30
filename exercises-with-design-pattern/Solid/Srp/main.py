class Book:
    """Represents a book with a title, author, and publication year."""
    def __init__(self, title: str, author: str, publicationYear: int):
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
    
    def __repr__(self):
        return (f"Book(title='{self.title}', author='{self.author}', "
                f"publicationYear={self.publicationYear})")
        
        
class BookRepository:
    def __init__(self):
        self._books: list[Book] = []
        
    def add_book(self, book: Book) -> None:
        """Adds a book to the collection."""
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        """Removes a book by title."""
        self._books = [book for book in self._books if book.title != title]

    def get_all_books(self) -> list[Book]:
        """Returns the complete list (for use by other services)."""
        return self._books
    
    def get_total_number_of_books(self) -> int:
        """Returns the total count."""
        return len(self._books)
    

class LibraryQuery:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_book_by_title(self, title: str) -> Book | None:
        """Finds a book title."""
        books = self.repository.get_all_books()
        return next((book for book in books if book.title == title), None)

    def get_books_by_author(self, author: str) -> list[Book]:
        """Returns a list of books by an author."""
        books = self.repository.get_all_books()
        return [book for book in books if book.author == author]

    def get_books_by_publication_year(self, publicationYear: int) -> list[Book]:
        """Returns a list of books published in a specific year."""
        books = self.repository.get_all_books()
        return [book for book in books if book.publicationYear == publicationYear]
    

if __name__ == "__main__":
    # Instantiate the Repository
    book_repo = BookRepository()

    # Instantiate the Query Service
    query_service = LibraryQuery(book_repo)

    # Add Books 
    book1 = Book('Clean Code', 'Edric Cao', 2023)
    book2 = Book('Design Pattern', 'Edric Cao', 2022)

    book_repo.add_book(book1)
    book_repo.add_book(book2)

    # Query Books
    print("Book by Title:")
    print(query_service.get_book_by_title('Clean Code')) 

    print("\nBooks by Author 'Edric Cao':")
    print(query_service.get_books_by_author('Edric Cao')) 

    # Get Total and Remove
    print(f"\nTotal books before removal: {book_repo.get_total_number_of_books()}")

    book_repo.remove_book('Design Pattern')

    print(f"Total books after removal: {book_repo.get_total_number_of_books()}")