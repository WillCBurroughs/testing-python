#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 21:02:25 2024

@author: williamburroughs
"""
import tkinter as tk
from tkinter import messagebox

from simple_fibonacci_functions import (
    select_fib_type, write_information_out, continue_fibonacci
)

def on_calculate():
    user_input = input_entry.get()
    if not user_input.isdigit():
        messagebox.showerror("Invalid input", "Please enter a valid number")
        return

    user_input = int(user_input)
    selected_option = fib_option.get()

    current_return = select_fib_type(selected_option, user_input)
    result_label.config(text=current_return)

def main():
    global input_entry, result_label, fib_option
    
    window = tk.Tk()
    window.title("Fibonacci Calculator")

    tk.Label(window, text="Enter the value:").grid(row=0, column=0)
    input_entry = tk.Entry(window)
    input_entry.grid(row=0, column=1)

    tk.Label(window, text="Select option:").grid(row=1, column=0)
    fib_option = tk.StringVar(value="1")
    tk.Radiobutton(window, text="Get xth fib value", variable=fib_option, value="1").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(window, text="Get all first x fib values", variable=fib_option, value="2").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(window, text="All fibs up to x value", variable=fib_option, value="3").grid(row=3, column=1, sticky="w")

    calculate_button = tk.Button(window, text="Calculate", command=on_calculate)
    calculate_button.grid(row=4, column=1)

    result_label = tk.Label(window, text="")
    result_label.grid(row=5, column=1)

    window.mainloop()

if __name__ == "__main__":
    main()
    
    # Add ability to save result, add memoization 
    # Add ability to add multiple rows of values (like calling get_first_fibs in for loop)