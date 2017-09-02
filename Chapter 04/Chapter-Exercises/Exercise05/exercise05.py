"""
Write a function that convers a string to a float and returns the result.
Use exception handling to catch the exception that could occur.
"""


def to_float(x):
    try:
        print(float(x))
    except(ValueError):
        print("Invalid value entered.")


value = input("Enter a floating point value: ")
to_float(value)
