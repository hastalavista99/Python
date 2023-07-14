"""
    Conditional Operators;
    > - greater than
    >= - greater than or equal to
    < - less than
    >= - less than or equal to
    = - assignment operator
    == - equality operator
    != - not equal
"""

# IF statement

# a = int(input("enter the first number: "))
# b = int(input("enter the second number: "))

# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else:
#     print("a is equal to b")

# or keyword can be used in an if statement containing more than one condition as follows

# if a > b or a < b:
#     print("a is not equal to b")
# else:
#     print("a is equal to b")


# MATCH statement
# the | character is the OR character
# the case _: is the deafult case

name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")



