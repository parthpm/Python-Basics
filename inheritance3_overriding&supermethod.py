
class Parent:
   def myMethod(self):
        print ('Calling parent method')
        self.value=15
        print(self.value)

class Child(Parent):
   def myMethod(self):
        self.value=20
        print ('Calling child method')
        print(self.value)
   def fun(self):
        print(self.value)
        super().myMethod()

p=Child()
p.myMethod()
p.fun()
