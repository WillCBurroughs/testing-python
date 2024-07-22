#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:02:25 2024

@author: williamburroughs
"""

def main():
    continue_fib = True
    while(continue_fib):
        invalid = True
        
        # This will determine if input is valid 
        while(invalid):
            try:
                user_input = int(input("What value would you like to go to? "))
                invalid = False
            except:
                print("Invalid input")
        
        # Ask user what type of fibonacci values they would like 
        selected_return = input("What type of fib would you like? 1. Get xth fib value, 2. Get all first x fib values, 3. All fibs up to x value ")
        current_return = ""
        
        # Testing user's input, turn to function 
        current_return = select_fib_type(selected_return, user_input)
        
        # Turn this to function 
        write_information_out(current_return)
        
        continue_fib = continue_fibonacci()
                
    print("Thank you for using the fibonacci calculator!! ")
    
def get_fib(value):
    first_fib = 0
    second_fib = 1
    hold_fib = 0
    iteration = 1
    
    while(iteration < value):
        hold_fib = first_fib 
        first_fib = second_fib
        second_fib = hold_fib + second_fib
        iteration += 1
        
    return first_fib

# Used to write to file 
def write_to_file(file_name, file_information):
    try:
        with open(file_name, "w") as fhand:  # Use 'with' to ensure the file is properly closed
            fhand.write(file_information)
    except Exception as e:  # Catch-all for exceptions
        print("Something went wrong:", e)
        
# Used to add text to file 
def add_to_file(file_name, file_information):
    try:
        with open(file_name, "a") as fhand:  
            fhand.write("\n" + file_information)
    except Exception as e:  # Catch-all for exceptions
        print("Something went wrong:", e)

# This will get the first x amount of fib values
def get_first_fibs(value):
    return_values = []
    total_values = 0
    
    #Get every value up to these values 
    while(total_values < value):
        return_values.append(get_fib(total_values))
        total_values += 1 
    
    return return_values

# This will get all the values up to x fib
def get_all_vals_up_to_x(value):
    return_values = []
    continue_fib = 0
    
    while(value >= get_fib(continue_fib)):
        return_values.append(get_fib(continue_fib))
        continue_fib += 1 
        
    return return_values
        
# Control flow for selecting fibonacci tyoe
def select_fib_type(selected_return, user_input):
    if selected_return == "1":
        current_return = str(get_fib(user_input))
    elif selected_return == "2":
        current_return = str(get_first_fibs(user_input))
    elif selected_return == "3":
        current_return = str(get_all_vals_up_to_x(user_input))
    else:
        print("Invalid option")
    print(current_return)
    return current_return 
        

# Control flow for writing info
def write_information_out(current_return):
    user_save = input("Would you like to write this information? y/n ")
    if user_save.lower() == "y":
        file_name = input("What name would you like to save the file to? ")
        write_or_append = input("Would you like to: 1. Add this to a text file 2. Write a new file ")
        if write_or_append == "1":
            add_to_file(file_name, current_return)
        else:
            write_to_file(file_name, current_return)

# Used to decide if user should continue 
def continue_fibonacci() -> bool:
    invalid_continue = True

    # Determines if user desires to continue
    while invalid_continue:
        continue_string = input("Would you like to continue? y/n ").lower()
        if continue_string in ("y", "n"):
            invalid_continue = False
            if continue_string == "n":
                return False
            else:
                return True

if __name__ == "__main__":
    main()
    
     
    # Turn control flow into functions, Add imports from other files, Add UI Component, add memoization 
    # Add ability to add multiple rows of values (like calling get_first_fibs in for loop)
    
    
    
    
    
    