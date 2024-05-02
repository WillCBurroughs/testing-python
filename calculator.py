
continue_running = True


while continue_running:
    firstValue = int(input("What is first Number? "))
    secondValue = int(input("What would you like for second Number? "))

    math_operation = int(input("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division "))

    if math_operation == 1:
        print(firstValue + secondValue)
    elif math_operation == 2:
        print(firstValue - secondValue)
    elif math_operation == 3:
        print(firstValue * secondValue)
    elif math_operation == 4:
        print(firstValue / secondValue)

    continue_running = input("Continue Running? y/n ")

    if continue_running.upper() == "Y":
        continue_running = True
    else:
        continue_running = False
    