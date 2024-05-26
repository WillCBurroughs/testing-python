class Student:
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError("Missing Name")
        self.name = name 
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name,house,patronus)
    

if __name__ == "__main__":
    main()