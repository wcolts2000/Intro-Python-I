# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


# def is_even(num):
#     if num % 2 == 0:
#         print('Even!')
#     else:
#         print('Odd')
#     return

# def is_even(num):
#     return num % 2 == 0


# lambda function version
def is_even(num): return num % 2 == 0


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# if is_even(num):
#     print('Even!')
# else:
#     print('Odd')

# Ternary Version
print('Even') if is_even(int(num)) else print('Odd')
