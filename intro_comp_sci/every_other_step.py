#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:29:24 2024

@author: williamburroughs
"""

def main():
    test_words = input("What words would you like to test? ")
    step_length = int(input("You would like what step between words? (ex 2,3,4) "))
    
    print(print_every_other(test_words,step_length))
    
def print_every_other(input_words, step):
    hold_words = input_words.split()
    hold_step = 0
    return_words = []
    
    for word in hold_words:
        hold_step += 1
        if hold_step % step == 0:
            return_words.append(word)
            
    return return_words

if __name__ == "__main__":
    main()