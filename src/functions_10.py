# Write a function is_even that will return true if the passed-in NUMber is even.
"""even vs odd"""
# YOUR CODE HERE

def is_even(num):
    """define even"""
    if num % 2 == 0:
        return True

# Read a NUMber from the keyboard
NUM = input("Enter a number: ")
NUM = int(NUM)

# Print out "Even!" if the NUMber is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(NUM) == True:
    print("Even!")
else:
    print("How Odd!")
