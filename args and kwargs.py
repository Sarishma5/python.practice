# techniques that enhance the adaptability of functions, making them more versatile and ready for different scenarios.
def total(x, y, z):
  return x + y + z

#When calling a function, you need to use the same number of arguments that have been defined, in the same order.

def total(x, y, z):
  return x + y + z

print(total(2, 1, 3))


#f the number of arguments of your function is unknown and unpredictable, you can always use an iterable as an argument.
def total(nums):
  result= 0
  #iterating over the list
  for i in nums:
    result+= i
  return result

num= [1, 2, 3, 4, 5]
print(total(num))  

#*args allows you to provide any number of arguments without the need to create a list before calling the function each time.

def total(*args):
  result = 0
  for arg in args:
     result += arg
  return result

print(total(1, 2, 3, 4, 5))
print(total(3, 5, 7, 8, 9))

#args receives arguments as a tuple, which can be used inside the function.

#Tuples are iterable 

#Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer.

def total(*prices):
  result = 0
  for arg in prices:
     result += arg
  return result

print(total(1, 2, 3, 4, 5))


def display(*words):
  for item in words:
    print(item)
display("paper", "pen", "pencil")

#When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition.

#Python also allows you to pass keyword arguments using **kwargs. 
# In this case, **kwargs receives arguments in the form of a dictionary, consisting of key:value pairs.

def display_info(**kwargs):
  for key, value in kwargs.items():
    print (key, " : ", value)

display_info(name="sarishma ", age= 21, city= "ktm")


# 🌟 *args enables you to pass an arbitrary number of positional arguments to a function

# 🌟 **kwargs allows you to pass keyword arguments to a function

# 🌟 *args collects arguments into a tuple, while **kwargs groups them into a dictionary with key:value pairs

# 🌟 'args' and 'kwargs' are conventional names, but you can use any names you prefer for these


def some_decorator(func):
    def wrapper(*args, **kwargs):
        # Pre-function execution logic (if any)
        result = func(*args, **kwargs)
        # Post-function execution logic (if any)
        return result
    return wrapper


