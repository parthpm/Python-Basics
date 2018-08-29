class Kettle(object):
    #class attributes
    power_source = "electricity"

    def __init__(self, make, price,units=5):
        self.make = make
        self.price = price
        self.on = False
        self.units=units

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
kenwood.price = 12.75

hamilton = Kettle("Hamilton", 14.55)

print("Models: {0} = {1}, {2} = {3}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print (kenwood.power)
# print(hamilton.power) error

#class objects does not have access to class attributes defined common for all classes
#when tried to access it creates local variable

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__) # powersource is not avaible 
