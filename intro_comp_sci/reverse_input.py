#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:51:53 2024

@author: williamburroughs
"""

def main():
    user_input = input("What words would you like to reverse? ")
    print(give_reverse(user_input))
    
def give_reverse(words):
    return words[::-1]

if __name__ == "__main__":
    main()