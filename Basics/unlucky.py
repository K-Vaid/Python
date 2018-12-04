# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:40:43 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""

user_input = input("Enter (,) seperated no.'s: ").split(",")

list_of_integers = list( map( int, user_input ) )

previous_number_is_13 = False
total = 0

for number in list_of_integers:
    if number == 13:
        previous_number_is_13 = True
    
    elif not previous_number_is_13:
        total += number
    
    elif previous_number_is_13 and number != 13:
        previous_number_is_13 = False

print (total)


############################################
##            Another way                 ##
############################################

'''
total = 0

for index in range( len( list_of_integers ) ):
    # checks if current number or previous number is 13
    if (list_of_integers[index] == 13 or list_of_integers[index-1] == 13):
        continue
    total += 1

print (total)
'''