class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last


    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name2):
         first,last=name2.split(' ')
         self.first=first
         self.last=last
    @fullname.deleter
    def deleter(self):
        self.first=None
        self.last=None
        print("Full name delter")

e1=Employee('Parth','Maheshwari')
print(e1.email)
print(e1.fullname)
e1.fullname='Parth PPM'
print(e1.fullname)
print(e1.first)
print(e1.last)
