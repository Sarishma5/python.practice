# How the Recursion Works
# Let's trace the execution when recursion(6) is called:

# First Call: recursion(6)

# n = 6 (which is greater than 0), so the function calls recursion(4):
# result = 6 + recursion(4)
# Second Call: recursion(4)

# n = 4 (still greater than 0), so the function calls recursion(2):
# result = 4 + recursion(2)
# Third Call: recursion(2)

# n = 2 (still greater than 0), so the function calls recursion(0):
# result = 2 + recursion(0)
# Base Case: recursion(0)

# n = 0, which triggers the base case, so the function returns 0.
# Now, the function starts returning from the recursive calls and prints the results:

# Returning from recursion(2):

# result = 2 + recursion(0) = 2 + 0 = 2.
# It prints 2.
# Returning from recursion(4):

# result = 4 + recursion(2) = 4 + 2 = 6.
# It prints 6.
# Returning from recursion(6):

# result = 6 + recursion(4) = 6 + 6 = 12.
# It prints 12.

n= int(input("enter the no: "))

def recursion(n):
    if(n>0):
        result= n + recursion(n- 2)
        print (result)
    else:
        result= 0
    return result
    
print("recursion result")
recursion(n)



