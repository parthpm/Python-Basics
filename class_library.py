class Book(object):
    def __init__(self,name,author=None,pages=0):
        self.name=name
        self.author=author
        self.pages=pages



class Customer(object):
    def __init__(self):
        self.book=[]

    def totalbooks(self):
        for b in self.book:
            print(b.name)
    def borrow(self,bookname):
        if bookname.name not in self.book:
            self.book.append(bookname)
            print("Total Books:",end='')
            self.totalbooks()
        else:
            pass



    def returnmethod(self,bookname):
        self.book.remove(bookname)
        print("Total Books:")
        self.totalbooks()


class Library(object):
    def __init__(self,books):
        self.books=books

    def display_book(self):
        for book in self.books:
            print(book.name)

b1=Book('C programming')
b2=Book('Java Programming')
b3=Book('Python Programming')
library=Library([b1,b2,b3])

library.display_book()
customer=Customer()
customer.borrow(b1)
customer.borrow(b2)
customer.returnmethod(b1)





