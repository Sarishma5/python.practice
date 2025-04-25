#In the real world, most things have a 'blueprint' and multiple instances of it. 
# By 'blueprint,' we refer to an abstract set of properties and behaviors. 
# Take, for example, a 'car.' It's a blueprint, or a general idea, covering properties like having four wheels, a color, engine power, and so on. 
# The cars you see on the road are specific instances of this general blueprint, each with its unique characteristics like color, make, and model.

# Abstraction of a Car: class
# A Green Car on a website: object



# To add attributes to a class, you must define the __init__ method.
#  This method's first parameter is always self, which represents the instance of the class.
#  Following self, you specify the attributes you wish to include. Then, inside the function, you assign values to the initialized object's attributes, setting their initial state.
class Car:
    #initialize attributes
    def __init__(self, brand, color):
        #assign values to attribute
        self.brand= brand
        self.color = color
#create the object of Car class
my_car= Car("Audi", "yellow")

print(my_car)
print(my_car.brand)
print(my_car.color)

my_car1 = Car('Toyota', 'green')

print(my_car1.brand)


class Car():
  def __init__(self, brand, model, color):
    self.brand = brand
    self.model = model
    self.color = color


my_car = Car('Toyota', "    ",'green')

print(my_car.brand)


# In addition to attributes, you can add custom behaviors to a class by defining functions within it.
#  These functions, known as methods, should include the 'self' parameter to interact with the class instance. 
# You can call these methods using the dot . notation, similar to how you access attributes.


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def honk(self):
        print("beep beep!")
        # No return needed unless you specifically want to return something

my_car = Car("audi", "pink")
my_car.honk()  # Output: beep beep!


