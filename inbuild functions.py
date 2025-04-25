# Functions are reusable blocks of code for specific tasks.
#  They help keep your code as short and easy to work with as possible,
#  saving you from repeating code.

#print(), input(), and type() are functions.

range(3)

#A function can take multiple arguments.

print("sarishma ", 23)

#print() and range() are examples of built-in functions.


x = "air"
y = "plane"
print(x + y)


balance = 304
print("Money in account:", balance)

print (range(3))


num = '45' # string
print(int(num) + 3)

# 🌟 You can use variables as arguments for functions

# 🌟 A function can be an argument for another function

# 🌟 Some functions require specific data types as arguments


print("bmw".upper())

#The capitalize() function will save you time when you need to convert the first character of a string to uppercase, 
# while making the remaining characters lowercase.

city = "BERN"
print(city.capitalize())

#The find() function checks if a character (or a pattern of characters) is present in a string. 
# The function returns the index (position) of the given value.
#  If the given value is present multiple times, the function will return the first occurrence (the lowest index).

print("robot".find("o"))

print("robot".find("A"))

item = "pen"
print(item.find("e"))

word = 'vehicle'
print(word.find('r'))

# word = 'vehicle'
# print(word.find())

# 🌟 upper(), lower(), and capitalize() functions are used to change the case of a string

# 🌟 The find() function searches for a value in a string and returns the index of the first time it appears

#len() stands for length and, when used on lists, it returns the number of items in the list.

movie = "Avatar"
print(len(movie))

#The append() function adds a new item to the end of a list. 

movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])

#The insert() function allows you to add an element to a list, at a specific position.
colors = ["Red", "Blue", "Yellow"]
colors.insert(0, "green")

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])

#The pop() function removes an element from a list.

topic = ["Maths","English","Physics"]
topic.pop(2)
print(topic)

 

# 🌟 len() returns the number of items in a sequence

# 🌟 append() adds an item to the end of a list

# 🌟 insert() and pop() add and remove list items at specific positions

