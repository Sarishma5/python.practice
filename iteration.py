# name= "points"
# value: 500

# print()

for i in range(3):
  print("First")
  print("Second")

for i in range(3):
  print("A")
print("B")

#the lack of indentation shows that the statement is outside the loop
for i in range(5):
  print("Hello")
print("Goodbye")

# As a general rule, when would you use a for loop? And a while loop?

# You know how many iterations: for loop
# You don’t know how many iterations: while loop

password = "SecretWord"
guess = "1234"
print(guess != password)


password = "SecretWord"
guess = input()
while guess != password:  
  guess = input() 
# print("Access Granted")

for box in range(50):
  print("Package A")
print("Task complete")

