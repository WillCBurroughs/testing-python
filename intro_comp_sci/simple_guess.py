# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

user_guess = int(input("Guess a number between 1 and 10 "))
actual_num = random.randint(1, 10)

while actual_num != user_guess:
    if actual_num > user_guess:
        print("Your guess was too small")
    else:
        print("Your guess was too large")
    user_guess = int(input("Guess a number between 1 and 10 "))
        
print("Congradulations! you guessed the number")