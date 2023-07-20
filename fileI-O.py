# file I/O is used to save program output to files in the system
# the open() function is used to open files and takes the file name as the parameter, and the mode the file will be opened with, "w" for write, "a" for append and "r" for read-only mode

# name = input("what's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# the program below outputs the contents of the file
# the rstrip() function is used to remove white space
# with open("names.txt", "r") as file:
#     for line in file:
#         print(line.rstrip())
#

# now lets store the file contents into a list

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")
