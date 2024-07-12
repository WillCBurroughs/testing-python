#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:00:53 2024

@author: williamburroughs
"""

def main():
    test_words = input("What words would you like to test? ")
    print(reverse_words(test_words))
    
def reverse_words(words):
    
    if len(words) <= 1:
        return words
    
    return reverse_words(words[1:]) + words[0] 

if __name__ == "__main__":
    main()