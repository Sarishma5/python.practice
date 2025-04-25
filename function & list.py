# #While developing applications, you’ll often work with functions that handle various data types.

# message = "Welcome"
# def greeting(text):
#   print(text)
# greeting(message)

# #You can create a custom function that takes a list as an argument

# my_menu=["pizza", "burger", "salad"]
# def show_menu(menu):
#   print(menu)
# show_menu(my_menu)


# #empty list
# new_menu= []

# #dishes for new menu
# dish1= "pasta"
# dish2= "chatpate"
# dish3= "noodles"

# #function defination
# def add_to_menu(menu, dish):
#    menu.append (dish)

# #adding dish1
# add_to_menu(new_menu, dish1)
# print(new_menu)

# #adding dish2
# add_to_menu(new_menu, dish2)
# print(new_menu)

# #adding dish3
# add_to_menu(new_menu, dish3)
# print(new_menu)


# menu=["dal bhaat", "chaumin", "momo"]
# def menu1(menu):
#    for dish in menu:
#      print(dish)

# menu1(menu)

# #You can take user inputs when calling a function.

# # This code prompts for user input each time the function is called, adding the entered value to the list:

# cart= []
# def add_to_cart(cart):
#    product= input(print("enter the product: "))
#    cart.append(product)

# add_to_cart(cart)
# print(cart)


# scores = []

# def add_score(scores):
#     score = int(input("Enter the score: "))
#     scores.append(score)

# add_score(scores)  # Pass the list 'scores' to the function
# print(scores)


# 🌟 functions can take lists as arguments

# 🌟 you can use for loops inside the a function to iterate through the list

# 🌟 you can take a user input when a function is called



####################################
#function and boolen
###################################

#In the world of programming, booleans are fundamental. 
# They represent the simplest form of data,
#  being true or false, and are crucial in decision-making processes within your code.

price = 50
print(price >= 50)
print(price < 50)

print(True and False)

delivery= True

def to_delivery(delivery):
    if delivery == True:
        # input(print("Enter your address"))
        print("Enter your address")

to_delivery(delivery)


# def my_function(score):
#   if score >= 70:
#     return True

# print(my_function(score))

def subject_offered(subjects, chosen):
  
    return  chosen in subjects

# Example usage:
subjects = ["Math", "Science", "History", "English"]
chosen = "Math"
print(subject_offered(subjects, chosen))  # Output will be True because "Math" is in the list

group= ["anisha", "nisha", "pinku", "sita", "gita"]
def check(group):
    if len(group)>5: # item is more then 5 so it return true
        return True
    else:
        return False # and false is displayed

print(check(group))

# 🌟 Functions can take booleans as arguments

# 🌟 Functions can return boolean values

# 🌟 You can use various tools to work with booleans inside functions


products = ['pen', 'pencil', 'ruler']
print(len(products))

#The sum() function takes a list as an argument and adds up all the elements in a list.

points = [51, 47, 99, 54]
total= sum(points)
print(total)

#The sum function can work only with lists with numerical values.
# values = ["1", "2", "3"]
# print(sum(values))

#The max() function returns the maximum value in a list.
prices = [33, 49, 55, 14]
max_price =max(prices)
print(max_price)

#The min() function returns the minimum value in a list.
prices = [33, 49, 55, 14]
print( min(prices))

ages = [22, 18, 19, 35]
print(len(ages))
print(max(ages))
print(min(ages))

#The sorted() function takes an iterable as input and returns a list with the items sorted.

ages= [1,34.29, 23, 49, 59, 100, 98, 94]

sorted_age= sorted(ages)
print(sorted_age)

prices = [503.9, 199.9, 254.5, 39.9]
srt_prices = sorted(prices)
print(srt_prices[1])

#The sorted() function can handle both numerical and textual values. 
# For textual values, it sorts them alphabetically.

players= ["akash", "anish","sarita", "jenisha", "bishnu","rajib"]
#sorting name
str_players= sorted(players)

print(str_players)
#When reverse = True, the values are sorted in descending order.
print(sorted(players, reverse= True))


ages = [25, 36, 33, 19, 56]
s_ages = sorted(ages, reverse= True)
print(s_ages)
print(s_ages[0:3])


# 🌟 the sum() function accepts a list as an argument and returns the sum of all its elements

# 🌟 the max() and min() functions return the maximum and minimum values from a list, respectively

# 🌟 the sorted() function is utilized for sorting lists in either ascending or descending order









