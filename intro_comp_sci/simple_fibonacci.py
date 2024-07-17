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
        while(invalid):
            try:
                user_input = int(input("What value would you like to go to? "))
                invalid = False
            except:
                print("Invalid input")
    
        print(get_fib(user_input))
        
        invalid_continue = True
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
    first_fib = 1 
    second_fib = 2 
    hold_fib = 0
    iteration = 0
    
    while(iteration < value):
        hold_fib = first_fib 
        first_fib = second_fib
        second_fib = hold_fib + second_fib
        iteration += 1
        
    return second_fib
    
if __name__ == "__main__":
    main()