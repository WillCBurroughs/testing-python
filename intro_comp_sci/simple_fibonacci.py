#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:02:25 2024

@author: williamburroughs
"""

from simple_fibonacci_functions import (
    select_fib_type, write_information_out, continue_fibonacci, set_input
)

def main():
    continue_fib = True
    while continue_fib:
        
        user_input = set_input()

        selected_return = input("What type of fib would you like? 1. Get xth fib value, 2. Get all first x fib values, 3. All fibs up to x value ")
        
        current_return = select_fib_type(selected_return, user_input)
        
        write_information_out(current_return)
        
        continue_fib = continue_fibonacci()
                
    print("Thank you for using the fibonacci calculator!! ")

if __name__ == "__main__":
    main()
    
    # Add UI Component, add memoization 
    # Add ability to add multiple rows of values (like calling get_first_fibs in for loop)
    
    
    
    
    
    