import unittest
import sys
from pathlib import Path

# Add the parent directory to the path to import from Solid/Srp/main.py
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Import from the SRP main module
from Solid.Srp.main import Book, BookRepository, LibraryQuery 



class TestBookRepository(unittest.TestCase):

    def setUp(self):
        self.repository = BookRepository()
        self.book1 = Book('Clean Code', 'Edric Cao', 2023)
        self.book2 = Book('Design Pattern', 'Edric Cao', 2022)

    def test_add_book(self):
        self.repository.add_book(self.book1)
        self.assertIn(self.book1, self.repository.get_all_books())

    def test_remove_book_by_title(self):

        self.repository.add_book(self.book1)
        self.repository.add_book(self.book2)
        self.repository.remove_book('Clean Code')
        
        self.assertNotIn(self.book1, self.repository.get_all_books())
        self.assertIn(self.book2, self.repository.get_all_books())

    def test_remove_book_nonexistent_title(self):

        self.repository.add_book(self.book1)
        self.repository.remove_book('Nonexistent Book')
        
        self.assertEqual(self.repository.get_total_number_of_books(), 1)
        self.assertIn(self.book1, self.repository.get_all_books())

    def test_get_total_number_of_books(self):
        self.repository.add_book(self.book1)
        self.repository.add_book(self.book2)
        
        self.assertEqual(self.repository.get_total_number_of_books(), 2)

    def test_get_all_books_empty_repository(self):
        self.assertEqual(self.repository.get_all_books(), [])


class TestLibraryQuery(unittest.TestCase):

    def setUp(self):
        # Create a repository and populate it with books for the search tests
        self.repository = BookRepository()
        self.book1 = Book('Clean Code', 'Edric Cao', 2023)
        self.book2 = Book('Design Pattern', 'Edric Cao', 2022)
        self.book3 = Book('Refactoring', 'Martin Fowler', 2018)
        
        self.repository.add_book(self.book1)
        self.repository.add_book(self.book2)
        self.repository.add_book(self.book3)
        
        self.search = LibraryQuery(self.repository) # Inject the populated repository

    def test_get_book_by_title(self):
        book = self.search.get_book_by_title('Clean Code')
        self.assertIsNotNone(book)
        self.assertEqual(book.author, 'Edric Cao')

    def test_get_book_by_title_not_found(self):
        book = self.search.get_book_by_title('Nonexistent Book')
        self.assertIsNone(book)

    def test_get_books_by_author(self):
        author_books = self.search.get_books_by_author('Edric Cao')
        self.assertEqual(len(author_books), 2)
        
        self.assertIn(self.book1, author_books)
        self.assertIn(self.book2, author_books)

    def test_get_books_by_author_not_found(self):
        author_books = self.search.get_books_by_author('Unknown Author')
        self.assertEqual(author_books, [])

    def test_get_books_by_publication_year(self):
        books_by_year = self.search.get_books_by_publication_year(2022)
        self.assertEqual(len(books_by_year), 1)
        self.assertEqual(books_by_year[0].title, 'Design Pattern')

    def test_get_books_by_publication_year_not_found(self):
        books_by_year = self.search.get_books_by_publication_year(1999)
        self.assertEqual(books_by_year, [])


if __name__ == '__main__':
    unittest.main()