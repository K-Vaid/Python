#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:02:50 2018

@author: dev
"""

'''
Code Challenge
  Name: 
    Temperature of City
  Filename: 
    city_temp.py
  Problem Statement:
    Print the temperature of your city in Degree Celsius for the day  
  Hint: 
     Use \u00b0 as the unicode for Degree 
  Output:
    26° C
'''

# Enter your city temperature 
temp_input = input("Enter city temperature: ")

print (temp_input+u"\u00b0"+" "+"C")