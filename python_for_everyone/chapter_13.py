class PartyAnimal:
    def __init__(self):
        self.x = 0

    def party(self) :
        self.x = self.x + 1 
        print("So far", self.x)

def main():
    an = PartyAnimal()
    an.party() 
    an.party()


if __name__ == "__main__":
    main()