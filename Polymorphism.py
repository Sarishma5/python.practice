#Polymorphim= many forms
#   inheritance= an obj can be treated as parent class
#   duck typing = obj must have necessary attribute/method
#


from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self): 
        pass


class Circle(Shape):
    def __init__(self, radious):   # this is constructor
        self.radious= radious
    
    def area(self):
        return 3.14* self.radious **2

class Square(Shape):
    def __init__(self, length):
        self.length= length
    
    def area(self):
        return self.length** 2

class Tringle(Shape):
    def __init__(self, base, height):
        self.base= base
        self.height= height
    
    def area(self):
        return self.base* self.height* 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radious):
        super().__init__(radious)
        self.toppiing= topping



# circle = Circle(4)
# square = Square(5)
# tringle = Tringle(6, 7)

shapes= [Circle(4), Square(5), Tringle(6, 7), Pizza("pepperoni", 4)]

for shape in shapes:
    print(f"{shape.area()}cm sqr")