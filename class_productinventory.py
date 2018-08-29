#Create an application which manages an inventory of products. Create a product class which has a price, id, and
# quantity on hand.
#  Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product(object):
    '''a class which has price,id and quantity
    '''
    def __init__(self,id,quantity,price):
        self.id=id
        self.quantity=quantity
        self.price=price

class Inventory()