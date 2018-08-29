class Circle(object):
    '''This is common to all objects'''
    #class object attribues or class atributes
    pi=3.14
    count=0

    def __init__(self,radius=1,perimeter=2*pi):
        self.radius=radius
        self.perimeter=radius*2*Circle.pi
        Circle.count+=1

    def area(self):
        return (self.radius**2)*Circle.pi

    def set_radius(self,new_radius):

        '''To reset radius
        '''
        self.radius = new_radius
        self.perimeter=self.radius*2*self.pi
    def __add__(self, other):
        return self.radius+other.radius
    @classmethod
    def set_pi(cls,value):
        cls.pi=value

c=Circle()
d=Circle()
print('Radius of default cirlce',c.radius,'\nPerimeter:',c.perimeter)
print(c.__doc__)

c.set_radius(15)
print('Radius of cirlce after updating',c.radius,'\nPerimeter:',c.perimeter)

print(c.count,'or ',Circle.count ,'no of circles created')
#class attributes
print(c.pi)
print(d.pi)
print(Circle.pi)
#setting value of pi to another
Circle.set_pi(1.0)
print(c.pi)
print(d.pi)
print(Circle.pi)
print(c+d)