# Functions in Python play a crucial role in enhancing the efficiency, reusability, and organization of code.

#Define the welcome() function and assign it to the greet variable
def welcome(name):
    return "welcome, "+ name
greet= welcome
print(welcome("sarita"))
print(greet("sarishma"))


def shout(text):  
    return text.upper()
yell = shout
print(yell("Hello"))


#Functions can take other functions as arguments.
def welcome(name):
    return "welcome, "+name

def process_user(name, func):
    return func(name)

print(process_user("saina", welcome))


def order(dish):
    return "Your order: " + dish

def process_order(dish, func):
    print(func(dish))

process_order("spaghetti", order)


# In Python, functions that operate with other functions — that is, take another function as an argument or return a function -  are called Higher-Order Functions. 
# They are particularly useful for processing various functions and returning specific results.
# name=input(print("enter ur name"))
def hello(name):
    return "what's up?, "+name

def bye(name):
    return "nice to meet u, bye see u again, "+ name

def process_user(name, func):
    return func(name)

print(process_user("sunita", hello))
print(process_user("gita", bye))


def book_title(title):
  return "Book title: " + title
def info(title, func):
  return func(title)

print(info("The Great Gatsby", book_title))


def total(price, count):
    return price*count
print(total(24, 34))


#Pure functions should always return the same result for the same inputs and not have side effects.
def welcome(user):
#   print("Welcome,", user)
    return "welcome "+ user
print(welcome("madhav"))

#The function is impure if it depends on any external state that it modifies or that affects its output. 
# This includes changing variables, or altering input arguments.
#  Such dependencies make the function's behavior unpredictable and dependent on the context in which it's run.

products= ["pen", "pencil", "paper"]
def add_items(product, item):
    products.append(item)

def hashtag():
  word = input()
  return '#' + word



# 🌟 You can assign a function to a variable and use it to call the function

# 🌟 Functions that take other functions as input and/or return a function are called Higher-order functions

# 🌟 Pure functions always return the same value for the same arguments and do not produce any side effects

