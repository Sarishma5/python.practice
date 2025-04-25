#In programming, bugs and errors are common, regardless of experience level.
#  They can range from minor typos to complex logical errors. 

#The computer reads and executes instructions line by line, from top to bottom. 
# The execution of the program will be interrupted at the first error encountered.

salary = 50000
role = "Analyst"
age = 29
print(salary)

#Mistakes in Python can be broadly categorized into two types: bugs and exceptions

#Bugs are flaws or mistakes in a program's code, leading to incorrect or unintended behavior.
#  This doesn't necessarily stop the program from running to completion,
#  but it can result in wrong outputs or behaviors.


#For example, the code below is meant to concatenate name and surname with a space. 
# It executes without error but omits the space, which indicates a bug.

name="mery"
surname="osborn"
print(name+ surname)

data = ["anna", "bob", "mery"]
names = [x.upper() for x in data]
print(names)


#Exceptions are another category of mistakes in programming.
#  These are specific errors that occur during a program's execution and
#  interrupt its normal flow when first encountered.


#For example, the program below will stop execution on the 2nd line:

# name= "bob"
# name[0]="R"
# print(name)


#The NameError exception is raised when an unknown variable is used.
# name = "Anna"
# print(surname)

city="ktm"
print("city: "+ city)


#The SyntaxError exception is raised when a syntax mistake in the code is encountered. 
# This could be due to various reasons such as missing punctuation (like commas, parentheses or colons).

score= 85
if score>= 80:
    print("passed")

#
#The IndexError is raised when you attempt to access an element of an iterable,
#  ordered collection, such as lists and tuples, using an index that is outside its valid range.

fruits=["orange", "apple", "banana ", "kiwi"]
print(fruits[3])


#The TypeError exception is raised when a function is called on a value of an inappropriate type.
#  For example, the len() function can be called only on iterables (like strings, lists, etc.).

# message= True
# len= len(message)
message= "hello"
length= len(message)
print(length)


#The ValueError exception is raised when a function receives a value of the correct type, 
# but the value itself is inappropriate or unacceptable.

#For example, the int() function can be called on strings,
#  but only when all characters in the string are numerical values.

data= "1189"
num_data= int(data)
print(num_data)

# 
# Match the exception types with their descriptions

# Incorrect syntax: SYNTAX ERROR
# Out-of-range index: INDEX ERROR
# Inappropriate value: VALUE ERROR
# Variable is not defined: NAME ERROR



# 🌟 Bugs are mistakes that may not interrupt execution but can cause incorrect behavior

# 🌟 Exceptions are errors that occur during execution and disrupt the program's flow

# 🌟 There are various types of exceptions




######################
#Exceptions handaling
#####################

#Exceptions often arise from a variety of causes, including invalid input,
#  out-of-bounds indices, incompatible type operations, and 
# logical errors in the code. 
# The good news is that exceptions are often predictable,
#  allowing developers to anticipate and handle them effectively.


#Type error
# prices = [250, 300, "240", 400]
# total = sum(prices)
# print(total)

# happy shopping will not be displayed
# prices = [250, 300, "240", 400]
# total = sum(prices)
# print(total)
# print("Happy shopping")


#
# Exceptions can often be predictable. 
# To handle them and prevent program failure,
#  you can use a try/except statement.

# The try block holds code that might cause an exception.
#  If an exception occurs, execution of the try block stops, and 
# the except block is executed, allowing the program to continue running.

prices= [120, 450, 560, "980", 670]
try:
    #block that may cuse an exception
    total= sum(prices)
    print(total)

except TypeError:
    #to perform if there ia exception
    print("Invalid data type")

print("happy shopping")


#If the execution of the try block encounters no exceptions, the except block will be

#not performed

color ="pink"
try:
    print(color)

except NameError:
    print("check the variable name")


color = "Green"
try:
  print(size)
except NameError:
  print("Check the variable name")



#When you specify only one type of exception to be handled, other types of exceptions will not be covered.
#  If these other exceptions occur, the program execution will fail.

# colors= ["red ", "pink", "blue", "purple"]
# try:
#    #index error
#    print(colors[10])

# #wrong exception
# except NameError:
#    print("error")

# #will not be executed
# print("life is colorful")

colors= ["red ", "pink", "blue", "purple"]
try:
   #index error
   print(colors[10])

#exception
except IndexError:
   print("error")

#will be executed
print("life is colorful")



#You can have multiple except blocks to handle each possible exception specifically.
#  As a best practice, it is recommended to output a definitive message for each type of handled exception.
colors= ["red ", "pink", "blue", "purple"]
try:
   #index error
   print(colors[10])

#exception
except IndexError:
   print("error")

except NameError:
   print("variable is not defined")

#will be executed
print("life is colorful")



try:
  print(len(5))
except NameError:
  print("Variable is not defined")
except TypeError:
  print("Not iterable")


#You can choose not to specify the exception type, which allows handling of any exceptions that may occur.

cars=["bmw", "tesla", "toyota"]
try:
   print(car[4])
except:
   print("error")


#Exceptions are very helpful when your program interacts with user input.
#While you can't control what a user inputs, you can control your program's behavior when the input doesn't match the expected format.
#

price= input()
try:
   price_value= int(price)
except:
   print("please enter the number")


choice = int(input())
coffees = ["latte", "macchiato", "espresso"]
try:
   print(coffees[choice])
except IndexError:
   print("Choose 0, 1, or 2")


# 🌟 Use a try/except block to handle exceptions and prevent program failure

# 🌟 If an exception occurs in the try block, the except block will be executed

# 🌟 You can handle exceptions without specifying the exception type




