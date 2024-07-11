#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:22:13 2024

@author: williamburroughs
"""

def main():
    
    valid_input = False
    continue_factorial = True
    
    while continue_factorial:
       while not valid_input:
           number_factorial = input("What value would you like the factorial of? ")
           if try_int(number_factorial):
               valid_input = True
               print(factorial(int(number_factorial)))
           else:
               print("Invalid input, put in integer value")
       continue_factorial = continue_factorials()
       if continue_factorial:
           valid_input = False 
           
    print("Thank you for using our factorial tester! ")
    

def factorial(value):
    if value <= 1:
        return 1
    
    return value * factorial(value - 1)

def try_int(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False

def continue_factorials():
    user_choice = input("Would you like to continue (y/n)? ")
    
    while user_choice.lower() != "y" and user_choice.lower() != "n":
        user_choice = input("Invalid input, continue? (y/n)? ")
    
    if user_choice.lower() == "y":
        return True
    else:
        return False

if __name__ == "__main__":
    main()