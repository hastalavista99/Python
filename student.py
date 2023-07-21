import csv
# the csv module provides functions for reading and editing csv files, eg. reader()that returns a list and DictReader() that returns a dictionary


students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


# the key parameter in the sorted function is used to specify the sorting criteria
# here we use lambda rather than defining an entire new get_name or get_house function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")


