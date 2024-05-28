class wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class student(wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the dark arts")