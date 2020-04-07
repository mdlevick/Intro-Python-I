"""Messing around with lists"""
# For the exercise, look up the methods and functions that are available for use
# with Python lists.

X = [1, 2, 3]
Y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change X so that it is [1, 2, 3, 4]
# YOUR CODE HERE
X.append(4)
print(X)

# Using Y, change X so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(X + Y)

# Change X so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(X + Y[1:])

# Change X so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

Y.insert(2, 99)

print(X + Y[1:])

# Print the length of list X
# YOUR CODE HERE

print(len(X))

# Print all the values in X multiplied by 1000
# YOUR CODE HERE
print([X[i] * 1000 for i in range(len(X))])
