import sys
print (sys.argv[3])


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

def add_book(id,title,author,year):
    book=Book(id,title,author,year)
    books.append(book)
    return books

def borrow_book(id):
    for book in books:
        if str(book.id)==id and book.available==True:
            book.available = False
            

def return_book(id):
    for book in books:
        if str(book.id)==id:
            book.available = True

def list_available():
    for book in books:
        if book.available == True:
            print(book)
# book=Book(123,"harry potter","JK rowing",2011)
add_book(123,"harry potter","JK rowing",2011)
add_book("124","mindset","unkown",2014)
print(books)
print("........")
list_available()
borrow_book("123")
list_available()