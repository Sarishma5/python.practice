#Data hiding is a key idea in making code with objects (like in games or apps) safer and cleaner.
#  It means keeping some parts of an object private so that only certain parts of your code can change them.
#  This helps prevent mistakes and keeps your code easy to manage.

#data hiding contributes to encapsulation in OOP, enhancing the security and robustness of your code.

class Car:
    def __init__(self, brand, year, odometer ):
     self.brand= brand
     self.year= year
     self.odometer= odometer

my_car = Car('Audi', 2020, 15000)
my_car.odometer = 20000

print(my_car.odometer)


# In Python, data hiding has two levels. The first involves prefixing an attribute with a single underscore _, signaling it's meant for internal use and should be viewed as 'protected'.

class Car:
  def __init__(self, model, year, odometer):
    self.model= model 
    self.year= year
    #making the odometer protected
    self._odometer = odometer

def describe_car(self):
  print(self.year, self.model)

def read_odometer(self):
  print("odometer: ", self._odometer, "miles")

my_car= Car("Audi", 2020, 15000)

my_car.describe_car()
my_car.read_odometer()

# Access the value of a protected attribute of my_account object
# my_account. _balance


class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer
