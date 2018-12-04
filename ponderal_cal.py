# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:45:40 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Ponderal Index Calculator
  Filename: 
    ponderal_cal.py
  Problem Statement:
    Calculate the Ponderal Index of a Person and print it
  Hint: 
    Divide the BMI by your Height ( meters ) to get your Ponderal Index
"""

# Enter your height in foot and inches
total_height = list(map(float,input("Enter your Height (like 5.11 (if it is 5 Foot and 11 inches)): ").split(".")))

# Enter your weight
weight = int(input("Enter your Weight in Kg: "))

if len(total_height) == 2:
    
    foot, inches = total_height

    # total height in foots
    total_foot = foot * 0.3048
    
    # total height in inches
    total_inches = inches * 0.0254
    
    # total height in meters
    total_height_in_meters = total_foot + total_inches

else:
    # total height in meters
    total_height_in_meters = total_height[0] * 0.3048

# Calculating BMI
BMI = (weight/total_height_in_meters)/total_height_in_meters

# Calculating Ponderal Index
Ponderal_Index = BMI/total_height_in_meters

print("\nYour Ponderal Index is: "+str(round(Ponderal_Index,2)))