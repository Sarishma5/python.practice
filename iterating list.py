#You can automate and
#  speed up the processing of a large amount of data if you know how to iterate over a list.

for i in range(3):
  print("Alarm")

products = ['milk', 'eggs', 'apples']

products = ['milk', 'eggs', 'apples']
print('bread' in products)

word = "movie"
print('o' in word)

products = ['milk', 'eggs', 'apples']
for i in products:
  print(i)

  
my_dict={x:
         x*2 for x in range(5)
         if x%2== 0
         }
print(my_dict)



#Nested loops, a concept where one loop operates within another, are crucial in programming.
#  Widely used in various real-world applications, 
# from game development to data analysis, nested loops are key to advancing your coding skills.

for i in range(3):
  print("New Message")

ranks = ["Ace", "King", "Queen"]
for rank in ranks:
  print(rank)

#A loop can have another loop nested within it. 
# This means that for each iteration of the outer (main) loop,the inner loop will run entirely.


# 

#This nested loop will display all possible combinations of ranks and 
# suits from the given lists:
ranks= ["ace", "king", "queen"]
suits= ["hearts", "clubs", "diamonds"]

for rank in ranks:
  for suit in suits:
    print(rank, suit)

#Each iteration of the outer loop runs the inner loop entirely, with corresponding iterator values.

vehicles = ['car', 'bike']
colors = ['red', 'blue']
for vehicle in vehicles:
  for color in colors:
    print(color, vehicle)

days = ['Monday', 'Tuesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
  for task in tasks:
    print(day, task )

#You can perform different actions for both inner and outer loops.
days = ['Monday', 'Tuesday', 'Wednesday']
tasks = ['Gym', 'Homework', 'Pool']
for day in days:
  print(day + ":")
  for task in tasks:
    print(task )

#When coding nested loops, it’s essential to maintain the correct indentation levels. 
# The instructions within each loop should be indented appropriately.

#You can create nested loops with ranges as well.

for i in range(1, 3):
  for j in range(2, 4):
    print(i, j )


#all possible pair combinations of numbers within the range of 1 to 2, inclusive
for i in range(1, 3):
  for j in range(1, 3):
    print(i,j)

signs = ["Red", "Yellow", "Green"]
for sign in signs:
  for i in range(3):
    print (sign)


#While building applications,
#  you'll encounter many situations where different programming concepts need to be combined to address a challenge.
#  One of the most common combinations is using iterations and selections.

#You can combine if statements with list iterations.

scores= [1,3,5,67,8,9 ,80]
for score in scores:
  if score>=9:
    print(score)

prices = [15, 66, 91, 143, 82, 102]
for price in prices:
  if price > 79:
    print(price)


for price in prices:
  if price < 30:
    print(price)


countries = ['US', 'France', 'Norway', 'Spain', 
  'US', 'France', 'US', 'Canada']
counter= 0
for i in countries:
   if i =='US':
     counter +=1
print(counter)

#You can use the for loop to iterate over strings,
#  which is handy for examining text data like looking for certain words or symbols.
message= "hello my dear friend"
count= 0
for i in message:
  if i== 'e':
     count +=1
print(count)


results = ['Hit', 'Miss', 'Miss', 'Hit', 'Miss']
count= 0
for i in results:
  if i== "Hit":
    count +=1
print(count)


animals = ['cat', 'turtle', 'tiger', 'dog', 'lion']
for i in animals:
  if 'r' in i:
    print(i)


# find the total sum of all the values in the given list
prices= [150, 79, 35, 259]
total = 0
for i in prices:
  total +=i
print(total)


points = [8.5, 7.9, 6.8, 8.2, 9, 6.3, 8.4]
count = 0
for i in points:
  if i> 8.0:
    count+=1
print(count)


#While developing applications, you’ll often work with
#  functions that handle various data types.

#Python has two main types of loops.

# Executing an action a specific number of times: for loop
# Executing an action while a condition remains true: while loop


seats= 3
while seats >0:
  print ("sell ticket")
  seats -=1


# The break statement is used to stop the loop when some condition is met.

# This is very useful when searching for a specific item or condition,
#  and there’s no need to continue once it’s found.

songs= ["hello", "yesterday", "happy", "hallelujah"]
for song in songs:
  if song== "happy":
    print("playing "+ song)
    break


prices = [35, 80, 16, 89, 95, 76]
for price in prices:
  if price > 90:
     break
  

prices = [35, 80, 16, 100, 95, 76]

for price in prices:
  if price > 90:
    break
  print(price)

#You can set any condition to exit the loop.

#For instance, in the provided code, the loop stops once the total price exceeds 100.

prices = [10, 15,30, 44, 45, 67]
total= 0
for price in prices:
  total += price
  print(total)
  if total >100:
    print("limit exceeded")
    break


#The break statement can be used with while loops as well.

#The loop in the provided code will stop when condition is meet

# while True:
#   text = input()
#   print(text)
#   if text == 'Stop':
#     break


# while True means the while loop's condition is always true, causing it to run indefinitely. 
# It will only stop when the condition for the break statement is met.


# while True:
#   print("text")

#The continue statement allows you to skip the 
# current iteration of a loop when a certain condition is true.

grades = [45, 80, 55, 90, 48, 60, 30]
for grade in grades:
  if grade >=50:
    continue
  print(grade)

#it will display items that don't start with l
animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l":
    continue
  print(animal)

#You can use the continue statement with while loops.

day_no=7
while day_no <=7:
  if day_no ==4:
    day_no +=1
    continue
  print("turn on the lights!")
  day_no +=1


#Code a while loop for a vending machine, 
# skipping the iteration when the hour is 5
hour = 1
while hour <= 10:
  if hour == 5:
    hour +=1
    continue
  print("making coffee")
  hour += 1


# 🌟 the break statement stops the loop when a specific condition is met

# 🌟 the continue statement skips the current iteration of the loop when a condition is me

# 🌟 these statements are used in conjunction with an if statement inside the loop


fruits = ['banana', 'orange', 'grape']
print('apple' in fruits)

movies = ["Avatar", "Matrix", "Fight Club"]
for i in movies:
  print(i)

for vehicle in vehicles:
  for color in colors:
    print(vehicle, color)

products = ['ball', 'gloves']
colors = ['red', 'blue']
for i in products :
  for j in colors:
    print(j, i)

colors = ['red', 'blue', 'green', 'yellow', 'purple']
for color in colors:
  if 'r' in color:
    print(color)

