"""
Write a function that takes three required parameters and two optional
parameters
"""


def doggo(name, age, sex, breed="mutt", good_boy=True):
    print("Your dog's name is: " + name)
    print(name + "'s age is: ", age)
    print(name + "'s sex is: " + sex)
    print(name + "'s breed is: " + breed)
    if good_boy:
        print(name + " is a good boy/girl")
    else:
        print(name + " is sorry for not being a good boy/girl!")


doggo("Pluto", 4, "Boy", "Black Lab")
