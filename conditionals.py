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

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")
