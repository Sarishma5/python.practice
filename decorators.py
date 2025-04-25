#decorators, special functions that modify or enhance other functions.

#A function that takes another function as an argument is called a higher-order function.


def song_name(name):
  return "Song name: " + name
def info(name, func):
  print(func(name))

info("Hallelujah", song_name)

#In the code above, the info() function takes a function as an argument.

#In Python, functions can be nested. This means you can define a function inside another function's body.

def greet(name):
  print("Hey", name)

  def welcome():
    print("Welcome onboard!")

    #return the result of the nested function directly from within the body of the parent function.
    msg= welcome()
    return msg

print(greet(" rohan"))


def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare()
  return status

print(order())


# Imagine you have a function that generates a message. Your goal is to create another function that takes this original function as an argument and converts the original message into uppercase, without altering the original function's code.

# These functions are known as decorators. In the code below, the uppercase() function acts as a decorator, and the wrapper() function represents the modified (or decorated) version of the greet() function.

def greet():
  return "welcome"

#take a function as an argument
def uppercase(func):
  #wrapper fun to keep the original fun code unchange
  def wrapper():
    org_msg= func()
    modified_msg= org_msg.upper()
    return modified_msg
  return wrapper

greet_upper= uppercase(greet)
print(greet_upper()) 


#decorators

#"they modify a function's behavior without altering its original code"

# ☑️ A function that modifies the original function
# (The decorator wraps the original function, adding behavior without altering its source code.)

# ☑️ A function as an argument
# (The decorator takes the original function (func) as an argument.)



# @light_decorator
# def watch_movie():
#   return "enjoy the movie"


# 🌟 Decorators are used to modify a function's behavior without altering its original code

# 🌟 You can use the '@' sign to apply a decorator to a function

# 🌟 The same decorator can be applied to a variety of functions


# @hashtag_decorator
# def add(word):
#   print(word)



def shout(text):  
  return text.upper()
yell = shout
print(yell("Hello"))


def order(dish):
  return "Your order: " + dish
def process_order(dish, func):
  print(func(dish))

process_order("spaghetti", order)



lambda word1, word2: word1 + word2