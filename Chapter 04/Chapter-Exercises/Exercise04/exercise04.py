"""
Write a program with two functions. The first function should take an integer as
a parameter and return the result of the integer divided by 2. The second
function should take an integer as a parameter and return the result of the
integer multiplied by 4. Call the first function, save the result as a variable,
and pass it as a parameter to the second function. 
"""


def half(x):
    """
    Returns x / 2.
    :param x: int.
    :return: float result of x / 2
    """
    return x / 2


def multiply(x):
    """
    Returns x * 4.
    :param x: int.
    :return: int product of x and 4
    """
    return x * 4


num1 = half(120)
num2 = multiply(num1)

print(num2)
