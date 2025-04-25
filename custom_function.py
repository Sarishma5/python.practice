#Built-in functions can save you a lot of work, 
# but you’ll also need to create your own custom functions to solve specific tasks.

# To use your own functions, you need to define them first. 

 

# Once a function has been defined, you can call it as many times as you need.

 

# The greet() function below contains code to display a nice message when called


def greet():
    print("hello rohan")
    print("good morning")

#function call
greet()

#A function might require arguments to complete its tasks. Arguments are put inside the parentheses () 
def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")

personal_greet("sarishma")

def double(no):
   print(no*  3)
double(3)

def bmi(weight, height):
    index = weight / (height * height)
    print(index)
bmi(37, 5.4)


#The result of a function can be sent back with the return statement.
#  This is particularly helpful when you need to continue using the result value in your program.

def bmi(weight, height):
  index = weight / (height * height)
  return index
p6 = bmi(79, 1.73)
print(p6 < 18.5)

# 🌟 def defines a new function

# 🌟 The function body contains the code that is executed when the function is called

# 🌟 return sends values back so they can be stored and used in the program


#Custom (or user-defined) functions help to break a large program down into small segments to make it easy to understand, maintain and debug.

#The function rect() helps a real estate agency calculate the area and perimeter of a rectangular parcel of land. 
# It takes the two dimensions of the parcel as arguments

def react(len, width):
   area= len *width
   parimeter= 2*len+ 2*width

   return area, parimeter #2 values

x, y = react(50, 100) # 2 veriable
print(x, y)


def rect(d1, d2):
  area = d1 * d2
  perimeter = 2 * d1 + 2 * d2
  price = 1000 * area
  return area, perimeter, price

a, pe, pr= rect(4, 5)
print(a, pe, pr)

#A function can return an error if something goes wrong in its body.
#  Passing argument values in the incorrect data type is a common source of errors. 

# It's up to you as a coder to define what operations happen inside your function. This then controls which data types can be handled and returned.

def profitable(d1, d2):
  area = d1 * d2
  invest = area > 700
  # return invest
profitable(23, True)
# print(profitable)


#The execution of the code inside a function ends when a value is returned. 
# Any additional lines of code after the return line will be ignored.

def rect(d1, d2):
  area = 0
  return area
  area = d1 * d2

  #Python allows function arguments to have default values. If the function is called without the argument, the argument gets its default value

def greet (name="guest"):
   print("welcome", name)
  
greet()
greet("rohan")

# 🌟 A function can return multiple values

# 🌟 Defining a function also decides the data types it can take in, handle and return

# 🌟 Default values make arguments optional


movies=["Avatar","Titanic","Alien"]
movies.append("Avengers")
movies.insert(2, "Terminator")
print(movies[3])


