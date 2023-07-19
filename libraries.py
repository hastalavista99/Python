# Libraries are files of code written to be used in programs
# Module is a library with one or more functions or features built into it, for reusability purposes
# We use the import keyword to get libraries from modules specified after it
# the from keyword specifies the fuction to be imported from the module

# RANDOM module

#from random import choice
import random

# the choice() function takes a list as the argument and returns a random element in the list
# the randint() function takes a starting and ending integer, all inclusive
# the shuffle() function takes a list as the argument and shuffles the elements in the lists

"""
coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)


cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


# STATISTICS module

import statistics
# the statistics module has a number of functions like mean(), median() etc that take a list as the argument and then performs the calculations

print(statistics.mean([100, 90]))
"""

# SYS module

# the sys module is used to catch command line arguments, or commands in the terminal before hitting the enter button
# the sys.argv[] takes a list as the argument

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")


for arg in sys.argv[1:]:
    print("Hello, my name is", arg)




