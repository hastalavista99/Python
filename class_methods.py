# class methods are those that dont have access to self but know which class they belong to, they take cls as an argument instead of self

import random

class Hat:

    # class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

# access class methods by using the class name followed by the method name, separated by a period
Hat.sort("Harry")
