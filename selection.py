age = 16
if age >= 18:
  print("Regular price")
else:
  print("Discount")

#After the computer has finished executing the if-else statement, it will continue to execute any following statements in sequence.


#You can build programs that make more complex decisions if you combine logical and comparison operations
is_student= True
age= 20
is_student or (age < 18)

print(is_student and (age < 18))


#####################################
#CONDITIONAL STATEMENT
############################
#Conditional statements allow you to program machines that make decisions.

age = 16
if age < 18: print("Apply Discount")
print("Proceed to Payment")

if age < 18:
  print("Junior discount")
elif age >= 75:
  print("Senior discount")
else:
  print("No discount")

age=17
is_student= False
if age< 18 and is_student:
  print("20% discount")
elif is_student== False:
  print("10 % discount")
else:
  print("regular price")
   

if age < 18:
  if is_student:
    print("20% discount")
  else:
    print("10% discount")
else:
  print("Regular price")

age = 29
if age < 18:
  if is_student:
    print("20% discount")
else:
  print("Regular price")
print("Proceed to payment")


# 🌟 skip the else statement when it is not needed

# 🌟 check for more conditions with the elif statement

# 🌟 nest if-else statements within each other


import time  # Import time module to use sleep function

heart_rate = 190  # Example heart rate

def vibrate():
    print("Vibrating...")  # This is where the vibration action happens

def wait(seconds):
    time.sleep(seconds)  # This will wait for the given number of seconds

def update_heart_rate():
    # Simulating heart rate change, for example by reducing it over time
    global heart_rate
    heart_rate -= 5  # Decrease heart rate by 5 each time (just for simulation)

# Main loop
while heart_rate > 180:
    vibrate()  # Trigger vibration
    wait(2)  # Wait for 2 seconds before checking again
    update_heart_rate()  # Simulate the heart rate dropping

print("Heart rate is below 180. Stopping the vibrations.")

for x in range(3):
  print("Repeat")
print("Stop")


#an infinite loop
# count = 1
# while count < 10:
#   print(count)

if heart_rate < 40: 
  print("Low heart rate")
elif heart_rate >= 180: 
  print("High heart rate")
else:
  print("Normal range")

seats = 5
while seats > 0:
  print("Sell ticket")
  seats= seats - 1