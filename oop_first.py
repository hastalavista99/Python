# an object is an instance of a class
# a method is a function inside a class
# the __init__ method is used to initialize objects, called everytime an object is created
# the __str__ method, when defined in a class, is automatically whenever an object wants to be seen as a string eg. when using print()
# the self argument gives access to the object that's just been created
# the raise keyword is used to raise errors without catching it, giving it a custom message

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def charm(self):
        match self.patronus:
            case "Stag":
                return "stag"
            case "Otter":
                return "otter"
            case "Jack Russel Terrier":
                return "jrt"
            case _:
                return "none"


def main():
    student = get_student()
    #print(f"{student.name} from {student.name}")
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()

