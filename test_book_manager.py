import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("1234567890", "Book 1", "Author 1")
        self.book2 = Book("0987654321", "Book 2", "Author 2")
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)

    def test_add_book(self):
        book3 = Book("1111111111", "Book 3", "Author 3")
        self.manager.add_book(book3)
        self.assertIn(book3, self.manager.books)
    
    def test_remove_book(self):
        self.manager.remove_book("1234567890")
        self.assertNotIn(self.book1, self.manager.books)
    
    def test_list_books(self):
        self.assertEqual(len(self.manager.list_books()), 2)

if __name__ == '__main__':
    unittest.main()
