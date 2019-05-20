"""positional argument function"""


def power(x, n=0):  # default value
    """function definition"""
    return x ** n


result = power(4, 5)  # call the function
print(result)
print(power(4))
