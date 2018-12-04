# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 16:06:46 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

import json


def fix_teen(number):
  teen_list = [13,14,17,18,19]
  if number in teen_list:
    return 0
  else:
    return number

def no_teen_sum ( dictionary ):
  list_of_numbers = dictionary.values()
  Sum = 0
  for number in list_of_numbers:
    Sum += fix_teen ( number )
  return Sum


input_dictionary = json.loads(input("Enter Dictionary: "))

print("Sum = " + str(no_teen_sum ( input_dictionary )))
