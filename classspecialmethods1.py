class Books(object):
    '''this is a class for creating books'''
    def __init__(self,author,name,pages):
        print("Book created:")
        self.author=author
        self.name=name
        self.pages=pages

    def __str__(self):
        return ("Title :{} \n Author :{} \n Total no pages: {}".format(self.name,self.author,self.pages))



    def __len__(self):
        return self.pages

    def __del__(self):
       print("Book deleted")
    def __add__(self, other):
        return self.pages+other.pages



b=Books(author='Bala',name='Python',pages=100)
c=Books(author='Balagurusamy',name='C++',pages=200)
print(b)
print(len(b))
print(b.__doc__)
print(b+c)

