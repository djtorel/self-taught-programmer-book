"""
Write a program with two functions. The first function should take an integer as
a parameter and return the result of the integer divided by 2. The second
function should take an integer as a parameter and return the result of the
integer multiplied by 4. Call the first function, save the result as a variable,
and pass it as a parameter to the second function. 
"""


def half(x):
    return x / 2


def multiply(x):
    return x * 4


num1 = half(120)
num2 = multiply(num1)

print(num2)
