# Dictionaries use key-value pairs
# the key-value pairs are wrapped in curly brackets, separated by commas

students ={
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# the keys in the dictionary act as indeces
# print(students["Harry"])
for student in students:
    print(student, students[student], sep=", ")
