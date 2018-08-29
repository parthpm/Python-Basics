class Sample(object):
    def display():
        print("This is a class")
x=Sample
print(type(x))
x.display()

class Dog(object):
    species='mammal'

    def __init__(self,breed,name,fur =False):
        self.breed=breed
        self.name=name
        self.fur=fur
    def barking(self):
        print(self.name," is barking.")
    def __str__(self):
        return "{0.breed}=Breed {0.name}=Name {0.fur}=Fur".format(self)

sam=Dog(breed='Pug',name='Rohan',fur=True)
print(type(sam))
print(sam.breed,' ',sam.name,' ',sam.species,' ',sam.fur)
print(Dog.__dict__) #dictionary containg class's namespace
print(sam.__dict__)
print(sam)

Dog.barking(sam) # calling from class

