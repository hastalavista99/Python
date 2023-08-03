# an object is an instance of a class
# a method is a function inside a class
# the __init__ method is used to initialize objects, called everytime an object is created
# the __str__ method, when defined in a class, is automatically whenever an object wants to be seen as a string eg. when using print()
# the self argument gives access to the object that's just been created
# the raise keyword is used to raise errors without catching it, giving it a custom error message
# getters and setters are used to specify the attributes of a value to avoid the user from entering just any value and prevent errors
"""
    A class method is a method that is bound to the class and not the object of the class. They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance. It can modify a class state that would apply across all the instances of the class
"""

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        # self.patronus = patronus

    # def charm(self):
    #     match self.patronus:
    #         case "Stag":
    #             return "stag"
    #         case "Otter":
    #             return "otter"
    #         case "Jack Russel Terrier":
    #             return "jrt"
    #         case _:
    #             return "none"

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    # # Getter
    # @ property
    # def name(self):
    #     return self._name

    # # Setter
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing name")
    #     self._name = name

    # # Getter
    # @property
    # def house(self):
    #     return self._house

    # # Setter
    # @house.setter
    # def house(self, house):
    #     if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
    #         raise ValueError("Invalid House")
    #     self._house = house


def main():
    student = Student.get()
    #print(f"{student.name} from {student.name}")
    print(student)

if __name__ == "__main__":
    main()

