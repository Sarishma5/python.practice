games = ["Snake", "Puzzle", "Chess"]

#Lists are incredibly useful in programming! They let you store multiple values in a single variable,
#  making your code more efficient.

products = ["apples", "oranges", "bananas"]
products[2] =  "lime"
print(products[2])

devices = ["TV", "Notebook", "PC"]
print(devices[1])

words = ["shelf", "store", "book"]

print(words[2] + words[0])

products = ["apples", "oranges", "bananas"]
products[1] =  "lime"
print(products[2])


#Indexing is a powerful technique that allows you to call part of a list.
name = "Lee"
country = "France"
user_info = [name, country]


products = ["juice", "chocolate", "water"]
user_choice = 1
print(products[user_choice])

# products= ["water", "papsi", "coke"]
# choice= int(input())
# print(products [choice])

#A string is a sequence of characters. 

animal = "Dog"
print(animal[0])

x = "arctic"
print(x[2] + x[0] + x[3])


#string are  immutable
# month = "august" 
# month[0] = "A"


#Slicing is a powerful technique that allows 
# you to precisely select data from a sequence.
animals =['cat', 'dog', 'bird', 'cow']
print(animals[2:4])

vehicle= "airplane"
print(vehicle[3:8])

colors = ['red', 'green', 'blue', 'yellow']
print(colors[1:3])

colors = ['red', 'green', 'blue', 'yellow']
print(colors[2:3])

fruit = 'orange'
print(fruit[0:2])

color = 'pink'
print(color[1:4])

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
print(planets[2:3])


a = [1, 2, 3] 
b = a 
b.append(4) 
print(a)

cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[:2])

vehicle = 'motorbike'
print(vehicle[:5])

cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[2:])

vehicle = 'motorbike'
print(vehicle[:])

platform = ['iOS', 'Android', 'Web']
print(platform[:])

planets = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets[2:])


char = ['A', 'B', 'C', 'D', 'E'] 
print(char[2:4])

#This code will output 3 ordered values in a list
planets = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets[:3])

planets = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets[2:])


#Indexing and slicing are incredibly useful,
#  allowing you to fully control the data you extract from sequences.

c = ['$', '£', '€', '¥']
print(c[-1])

vehicle = 'motorbike'
print(vehicle[-1])

#output the 2 last values
c = ['$', '£', '€', '¥']

print(c[-2:])

c = ['$', '£', '€', '¥']
print(c[1:3])
print(c[-1:-3])
print(c[2:])
print(c[3:])

print(c[1:-1])

print(c[0:-2])

c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)
c[:2] = ['₣', '฿']
print(c)



vehicle = 'motorbike'
print(vehicle[-4:])

# vehicle = 'airplane'
# vehicle[:3] = 'water'
# print(vehicle)

#string are immutable
# vehicle = 'airplane'
# vehicle[:3] = 'water' 

# word = "run"
# word[0] = "f"
# print(word)

brands = ["Honda", "Toyota", "BMW", "Mercedes"]
print(brands[1:3])
print(brands[-3:-1])

c = ['$', '£', '€', '¥']
print(c[-1])
print(c[-3:-1])
