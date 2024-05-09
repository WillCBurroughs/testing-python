# Simple dictionary format 
students = {
    "Hermione": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Draco": "Slytherin"
}

print(students)
print(students["Hermione"])

# Printing out keys and values
for student in students:
    print(student, students[student])


# Lists of dictionaries 
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    # None is keyword for designating not present 
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"])