def get_fib(value):
    first_fib = 0
    second_fib = 1
    hold_fib = 0
    iteration = 1
    
    while iteration < value:
        hold_fib = first_fib 
        first_fib = second_fib
        second_fib = hold_fib + second_fib
        iteration += 1
        
    return first_fib

def write_to_file(file_name, file_information):
    try:
        with open(file_name, "w") as fhand:  # Use 'with' to ensure the file is properly closed
            fhand.write(file_information)
    except Exception as e:  # Catch-all for exceptions
        print("Something went wrong:", e)
        
def add_to_file(file_name, file_information):
    try:
        with open(file_name, "a") as fhand:  
            fhand.write("\n" + file_information)
    except Exception as e:  # Catch-all for exceptions
        print("Something went wrong:", e)

def get_first_fibs(value):
    return_values = []
    total_values = 0
    
    # Get every value up to these values 
    while total_values < value:
        return_values.append(get_fib(total_values))
        total_values += 1 
    
    return return_values

def get_all_vals_up_to_x(value):
    return_values = []
    continue_fib = 0
    
    while value >= get_fib(continue_fib):
        return_values.append(get_fib(continue_fib))
        continue_fib += 1 
        
    return return_values

def select_fib_type(selected_return, user_input):
    if selected_return == "1":
        current_return = str(get_fib(user_input))
    elif selected_return == "2":
        current_return = str(get_first_fibs(user_input))
    elif selected_return == "3":
        current_return = str(get_all_vals_up_to_x(user_input))
    else:
        print("Invalid option")
        current_return = ""
    print(current_return)
    return current_return 

def write_information_out(current_return):
    user_save = input("Would you like to write this information? y/n ").lower()
    if user_save == "y":
        file_name = input("What name would you like to save the file to? ")
        write_or_append = input("Would you like to: 1. Add this to a text file 2. Write a new file ")
        if write_or_append == "1":
            add_to_file(file_name, current_return)
        else:
            write_to_file(file_name, current_return)

def continue_fibonacci() -> bool:
    invalid_continue = True

    while invalid_continue:
        continue_string = input("Would you like to continue? y/n ").lower()
        if continue_string in ("y", "n"):
            invalid_continue = False
            if continue_string == "n":
                return False
            else:
                return True

def set_input() -> int:
    invalid = True
    while invalid:
        try:
            user_input = int(input("What value would you like to go to? "))
            invalid = False
        except ValueError:
            print("Invalid input")
    return user_input
