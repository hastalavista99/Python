# print, string and int functions and methods
# input prompts the user
name = input("What is your name? ").strip().title()
# name = name.strip()# remove whitespace from str(incase of accidental spaces)
# capitalize the first letter with the capitalize method
# name = name.capitalize()
# name = name.title()# capitalize the first letter of each string
# split user's name into first name and last name
first, last = name.split(" ")
# age = input("What's your age? ")
# print("Hello,", name, ". Your are", age, "years old")
# print(*object, sep=" ", end"\n") default print positional parameters as per python documentation
# print("hello, ",end="") # this removes the default newline character and enables us to print both statements on a single line
# print("David")

# printing quotes inside other quotes by using single quotes inside double quotes or vice versa as follows
# print("hello, 'friend'")

# or use the escape character
# print("hello, \"friend\"")

# the statement below formats the name variable

print(f"hello, {first}")




