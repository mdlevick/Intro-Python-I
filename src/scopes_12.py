# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables
"""working with scopes"""
# When you use a variable in a function, it's local in scope to the function.
X = 12

def changex():
    """X scope"""
    global X
    X = 99

changex()

# This prints 12. What do we have to modify in change_X() to get it to print 99?
print(X)


# This nested function has a similar problem.

def outer():
    """Showing the difference between local and non local"""
    Y = 120

    def inner():
        """Y scope"""
        nonlocal Y
        Y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(Y)


outer()
