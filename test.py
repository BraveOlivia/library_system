import unittest
import library_system

class TestLibrary(unittest.TestCase):

    def test_book(self):
        book1=library_system.Book("123","Harry Potter","J. K. Rowling",1997)
        self.assertEqual(book1.author,"J. K. Rowling")

    def test_add_book(self):
        book2=library_system.add_book("124","Mindsets","Carol S Dweck",2008)
        self.assertEqual(book2.year,2008)

    def test_borrow_book(self):
        book2=library_system.add_book("124","Mindsets","Carol S Dweck",2008)
        book2=library_system.borrow_book("124")
        self.assertEqual(book2.available,False)


    def test_return_book(self):
        book2=library_system.add_book("124","Mindsets","Carol S Dweck",2008)
        book2=library_system.borrow_book("124")
        library_system.return_book("124")
        self.assertEqual(book2.available, True)

if __name__ == '__main__':
    unittest.main()