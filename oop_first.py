# an object is an instance of a class
# a method is a function inside a class
# the __init__ method is used to initialize objects, called everytime an object is created
# the self argument gives access to the object that's just been created

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.name}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()

