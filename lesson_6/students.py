students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")

        # Making dict of student to place
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

for student in sorted(students, key = lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in house {student['house']}")

