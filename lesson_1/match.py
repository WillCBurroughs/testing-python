name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
        
    # Default catch all case 
    case _:
        print("Who?")