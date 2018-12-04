# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 17:30:51 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Height Calculator
  Filename: 
    height_cal.py
  Problem Statement:
    Lets assume your height is 5 Foot and 11 inches 
    Convert 5 Foot into meters and 
    Convert 11 inch into meters and 
    print your total height in meters and 
    print your total height in centimetres also 
  Hint: 
    1 Foot = 0.3048 meters 
    1 inch = 0.0254 meters 
    1 m = 100 cm 
"""

# Enter your height
foot, inches = list(map(float,input("Enter your height (like 5.11 (if it is 5 Foot and 11 inches)): ").split(".")))

# total height in foots
total_foot = foot * 0.3048

# total height in inches
total_inches = inches * 0.0254

# total height in meters
total_height_in_meters = total_foot + total_inches

# total height in centimeters
total_height_in_centimeters = total_height_in_meters * 100

print("Total Height in Meters is "+str(round(total_height_in_meters,2))+" m")
print("Total Height in Centimeters is "+str(round(total_height_in_centimeters,2))+" cm")