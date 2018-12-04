# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:26:51 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Letters 6 
    Digits 2
"""

# accepting input from user, expected input to be combionation of
#lettters and numbers.
user_input = input("Enter string : ")

letters, digits = 0, 0       # initialising the counter for letter and digit

# loop to access every element of string individually.
for character in user_input:
    
    if character.isdigit():      # conditiion to check for digit.
        digits += 1      # if found increase counter variable by 1.

        
    elif character.isalpha():    # conditionto check for Letter.
        letters += 1      # if found increase counter variable by 1.
        

print ("Letters", letters)
print ("Digits", digits)
