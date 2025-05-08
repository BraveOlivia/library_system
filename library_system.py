import sys
# print (sys.argv)

# Book class with five attributes and a method to print out the detailed info of each book.
class Book:
    def __init__(self,id,title,author,year):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.available=True

    def __str__(self):
        return f"{self.id} {self.title} {self.author} {self.year} {self.available}"

books=[]

# Add a book to the books array
def add_book(id,title,author,year):
    book=Book(id,title,author,year)
    books.append(book)
    return book

# Borrow a book with the unique id
def borrow_book(id):
    for book in books:
        if str(book.id)==id and book.available==True:
            book.available = False
            return book
            
# Return a book with the id
def return_book(id):
    for book in books:
        if str(book.id)==id:
            book.available = True

# List all available books
def list_available():
    for book in books:
        if book.available == True:
            print(book)


# Test demo
book=Book(123,"harry potter","JK rowing",2011)
add_book(123,"harry potter","JK rowing",2011)
add_book("124","mindset","unkown",2014)
print(books)
list_available()
borrow_book("123")
list_available()
return_book("123")
list_available()