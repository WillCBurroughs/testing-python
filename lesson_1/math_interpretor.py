def main():
    user_math = input("What math would you like to perform? ")
    hold_user_math = find_values(user_math)

    print(perform_operation(hold_user_math[1], float(hold_user_math[0]), float(hold_user_math[2])))

def find_values(user_input):
    user_input = user_input.strip()
    hold_all_input = user_input.split(" ")
    return hold_all_input

def perform_operation(operator, first_value, second_value):
    if(operator == "+"):
        return first_value + second_value
    elif(operator == "-"):
        return first_value - second_value
    elif(operator == "/"):
        return first_value / second_value
    else:
        return first_value * second_value

main()