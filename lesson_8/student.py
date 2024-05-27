class Student:
    def __init__(self, name, house, patronus):
        if not name: 
            raise ValueError("Missing Name")
        self.name = name 
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell Terrier":
                return "🐕"
            case _:
                return "🪄"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name)
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name,house,patronus)
    

if __name__ == "__main__":
    main()