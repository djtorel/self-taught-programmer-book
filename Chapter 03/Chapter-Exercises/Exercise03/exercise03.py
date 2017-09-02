"""
Write a program that prints a message if a variable is less than or equal to 10,
another message if the variable is greater than 10 but less than or equal to 25,
and another message if the variable is greater than 25.
"""

num1 = 130

if num1 <= 10:
    print("num1 is <= 10")
elif num1 <= 25:
    print("num1 is > 10, but <= 25")
else:
    print("num1 is > 25")
