# Dictionaries use key-value pairs
# the key-value pairs are wrapped in curly brackets, separated by commas
"""
students ={
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# the keys in the dictionary act as indeces
# print(students["Harry"])
for student in students:
    print(student, students[student], sep=", ") # this prints the key and the value

"""

# below is a list whose elements are dictionaries
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
