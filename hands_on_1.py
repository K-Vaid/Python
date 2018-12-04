# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:19:47 2018

@author: Kunal Vaid

# Hands On 1  
# Make a function to find whether a year is a leap year or no, return True or False 
"""

def leap_year_finder(year):
    # Checking for leap year
    if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
        return "True"
    else:
        return "False"

inp = int(input("Enter year to check for leap year: "))
print(leap_year_finder(inp))


########## Pythonic Code ##########
'''
import calendar
print (calendar.isleap(inp))'''