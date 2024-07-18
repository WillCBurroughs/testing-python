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
        
        # Testing user's input
        if selected_return == "1":
            print(get_fib(user_input))
        elif selected_return == "2":
            print(get_first_fibs(user_input))
        else:
            print("Invalid option")
        
        invalid_continue = True
        
        # Determines if users desires to continue 
        while(invalid_continue):
            continue_string = input("Would you like to continue? y/n ").lower()
            if(continue_string == "y" or continue_string == "n"):
                invalid_continue = False 
                if(continue_string == "n"):
                    continue_fib = False
                else:
                    break
                
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

# This will get the first x amount of fib values
def get_first_fibs(value):
    return_values = []
    total_values = 0
    
    #Get every value up to these values 
    while(total_values < value):
        return_values.append(get_fib(total_values))
        total_values += 1 
    
    return return_values
    
    
if __name__ == "__main__":
    main()
    
    
    # Next things to add, option 3 - get all less than value x, Adding option to write to files, ability to choose file names make new ones (etc)
    # Add UI Component 
    
    
    
    
    
    