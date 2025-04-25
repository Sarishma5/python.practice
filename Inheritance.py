#principle of inheritance, an OOP concept that enhances your program's versatility and efficiency.

class Animal:
    def __init__ (self, name):
        self.name= name
    
    def movie(self):
        print("Moving")
    
#inherits from animal class
class Dog(Animal):
    #specific behavior
    def bark(self):
        print("woof!")

#creating an instance
my_dog = Dog("Bob")

#Inherited attribute and behavior
print(my_dog.name)
my_dog.movie()

#specific behavior
my_dog.bark()


# A class from which others are inherited is known as a superclass or parent class. 
# Conversely, a class that inherits from another class is referred to as a subclass or child class.

#The child class inherits all the attributes and methods of the parent class.



#parent class 
class Animal:
    def __init__(self, name):
        self.name= name

    def move(self):
        print("moving")

#child class
class Dog(Animal):
    def __init__(self, name, breed, age):
        #initialixze attribute of the superclass
        super().__init__(name)
        #additional attribute specific to dog
        self.breed= breed
        self.age= age

    def bark(self):
        print("woof!")

my_dog= Dog ("jax", "Bulldog", 4)
#inherited attribute
print(my_dog.name)

# addiional AttributeError
print(my_dog.breed)
print(my_dog.age)


#The child class inherits all the attributes and methods of the parent class.
#OVERRIDING

#parent class 
class Animal:
    def __init__(self, name):
        self.name= name
    
    #sound method for any animal
    def sound(self):
        print("making a sound")

#child class
class Dog(Animal):
    def __init__(self, name, breed, age):
        #initialixze attribute of the superclass
        super().__init__(name)
        #additional attribute specific to dog
        self.breed= breed
        self.age= age
    
    #overriding sound method for Dog
    def sound(self):
        print("woof!")

my_dog= Dog ("jax", "Bulldog", 4)
#inherited attribute
print(my_dog.name)


#Clild class Cat
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age= 3
    #overriding sound method
    def sound(self):
        #call the sound from Animal
        super().sound()
        #additional functionality for CAT
        print("meow!")

my_cat= Cat("billi", 12)


#using the overrriding method
my_dog.sound()
my_cat.sound()



#POLYMORPHISM
# Polymorphism lets objects use methods in their own way, even if they share the same name.

animals=[ my_dog, my_cat]
for animal in animals:
    animal.sound()
