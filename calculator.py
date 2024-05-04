
continue_running = True


while continue_running:
    first_value = float(input("What is first Number? "))
    second_value = float(input("What would you like for second Number? "))
    hold_result = 0
    firstValue = float(input("What is first Number? "))
    secondValue = float(input("What would you like for second Number? "))

    math_operation = int(input("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division "))

    if math_operation == 1:
        hold_result = first_value + second_value
    elif math_operation == 2:
        hold_result = first_value - second_value
    elif math_operation == 3:
        hold_result = first_value * second_value
    elif math_operation == 4:
        hold_result = first_value / second_value

    hold_result = round(hold_result, 2)
    print(f"{hold_result:,}")

    continue_running = input("Continue Running? y/n ")

    if continue_running.upper() == "Y":
        continue_running = True
    else:
        continue_running = False
    