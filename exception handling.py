
ages = [18, 24, 43, 56]
try:
    print(ages[10])
except IndexError:
    print("Out of range")

#  handling exception

#You can have multiple except blocks to handle each possible exception specifically.


#You can use the finally statement to perform an operation after the try/except block, no matter if an exception occurred or not.
prices= [559, 898, "sarita", 456]
try:
    print(sum(prices))
except TypeError:
    print("check the prices")
finally:
    print("need help? contact us")

try:
  print(len(3745))
except:
  print("Error")
finally:
  print("Save")


#The else statement can be used in conjunction with the try/except block and will execute only when no error occurs in the try block.
books= ["seto darti", "sumi", "summer love", "emma", "harry potter"]
try:
#    choice= books[int(input(print("enter the no 1to 4")))]
     choice=books[0]
except:
   print("out of range")
else:
   print(choice+ "is a great choice")


products = ['ball', 'toy', 'paper']
try:
  count = len(products)
except:
 print("Error")
else:
  print("Count of products:", count)


# books= ["seto darti", "sumi", "summer love", "emma", "harry potter"]
# choice= books[int(input(print("enter the no 1to 4")))]
# print(choice+ " is greate choice")


#You can trigger your own exceptions based on specific conditions using the raise statement.
#  This will immediately stop the program's execution and indicate an error has occurred.

# print("rate from 0 t0 100")
# rate= 15
# if rate>40 or rate< 0:
#    raise ValueError

# price = 995
# if price > 500:
#   raise ValueError

#Custom exceptions are really helpful when it comes to handling logical issues that can't be caught by the computer.

# rating= 15
# if rating> 10 or rating<0:
#    raise ValueError("Rate from 0 to 10")


# temp = -15
# if temp > 50 or temp < -10:
#   raise ValueError("Invalid range")


# 🌟 the finally keyword is used to execute code after a try/except block, regardless of whether an exception was raised

# 🌟 the else keyword, used with try/except, runs only if the try block is error-free

# 🌟 custom exceptions can be triggered using the raise keyword


try:
  print(3 + "3")
except ValueError:
  print("Cannot add different types")
except TypeError:
  print("Type mismatch error")


