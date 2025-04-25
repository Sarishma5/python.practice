# lambda expressions - efficient feature in Python,
#  allowing you to create compact, throwaway functions without needing the formal structure of a standard function definition.

def total(price, count):
  return price*count

print(total(2,3))

#we can assign function to the variable
def welcome(name):
  return "Welcome, " + name
greet = welcome


#Lambda expressions are functions without a name that are quick to create and use.
#  They are written in just one line using the lambda keyword and are often used for small, simple tasks.

greet= lambda name: "welcome "+ name
print(greet("sari"))

lambda x:x+5

# Lambda expressions are called anonymous functions. This means that:
# They don't need a name while being defined


#Lambda expressions perform a single operation and return a result.
# They are defined using the lambda keyword, followed by its arguments, a colon, and the expression to perform.

word= lambda word: "#"+ word
print(word("Happy"))


lambda price: price * 0.9
# argument: price
#expression: price*0.9


#You can assign the lambda expression to a variable and then call it as a regular function.
discount= lambda price: price*10
print(discount(100))

#Lambda expressions can take multiple arguments separated by commas.
lambda name, surname: name +surname

x = lambda price, count :  price * count
print(x(2,10))


#You can provide arguments to lambda expressions on-the-fly by adding them in parentheses immediately after the lambda function.
#  The lambda expression should be also enclosed in parentheses.

res= (lambda x, y: x+y)(1, 3)
print(res)


#The power of lambda is better shown when you use them as an anonymous function inside another function. 
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def mult(n):
  return lambda a:a*n

doubler=  mult(2)
tripler= mult(3)

print(doubler(4))
print(tripler(3))

 

# 🌟 Lambda expressions are compact, anonymous functions used for simple operations

# 🌟 Lambda expressions can be assigned to variables or used within other functions for on-the-fly operations


#The power of lambda expressions becomes evident when working with data manipulation and transformation tasks.



#The map() function applies a specified function to every element in an iterable, like lists or tuples. It produces a result that can be transformed into a list using the list() function for easy viewing or further use.

names= ["alisha", "anish", "ashish","anisha"]

#function to capitalize to eachname
def cap(name):
  return name.capitalize()

#using map() to apply the capitalize to each name
capi=  map(cap, names)

#conveting map object to a list
capi= list(capi)

print(capi)


prices = [25.99, 14.50, 8.75, 19.95]
def discount(price):
  discounted_price = price * 0.9
  return discounted_price

discounted_prices = list(map(discount, prices))

print(discounted_prices)


# The map function requires the first argument to be a function and the second argument to be an iterable.
scores=[45, 78,94, 67, 93,21]
def is_passing(score):
  return score>= 50

status= list(map(is_passing, scores))

print(status)


#Do you remember lambda expressions? Another valuable aspect of them is their ability to be directly provided to the map function.
#  This eliminates the need to define a regular function explicitly.

nums =[1, 3, 5, 7,8]
double= list(map(lambda x:x*2, nums))
print(double)


#The filter() function, just like the map() function, takes in a function and an iterable as arguments. 
# The key purpose of filter() is to apply a condition specified in the provided function to each item in the iterable and return only those for which the function evaluates to True.


# Transforms the items of an iterable: 
# map()
# Returns items that meet a condition: 
# filter()


names = ["John", "Emma", "Jake", "Rachel", "James"]
filtered = list(filter(lambda name: name[0] == 'J', names))
print(filtered)


# 🌟 The map() function applies a specified function to every element in an iterable

# 🌟 The filter() function filters out items from an iterable based on a specified condition

# 🌟 Both can accept lambda expressions as arguments


res = (lambda x, y: x*y) (4,2)
print(res)


scores = [5, 10, 15, 20]  # Example iterable

# Using map with a lambda function
result = list(map(lambda x: x + 10, scores))

print(result)  # Output: [15, 20, 25, 30]


fruits = ["apple", "banana", "cherry", "elderberry"]
fruits_filt = list(filter(lambda x: 'a' in x, fruits))
print(fruits_filt)