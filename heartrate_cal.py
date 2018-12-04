# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:04:37 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Target Heart Rate Calculator
  Filename: 
    heartrate_cal.py
  Problem Statement:
    Calculate the Maximum Heart Rate and Target Heart Rate Range 
    ( Lower and Higher value ) of a person of a specific age.
    Lets Assume your age is 21 years
  Hint: 
    Subtract your age from 220 to get your Maximum Heart Rate
    Lower end of your Target Heart Rate is 70% of Maximum Heart Rate
    Higher end of your Target Heart Rate is 85% of Maximum Heart Rate
    Heart Rate = Beats per minute 
"""
#Enter your Age
age = int(input("Enter your Age: "))

# Calculating Maximum Heart Rate
max_heart_rate =  220 - age

# Calculating Target Heart Rate (Lower)
target_heart_rate_lower  = max_heart_rate * 0.7

# Calculating Target Heart Rate (Higher)
target_heart_rate_higher = max_heart_rate * 0.85

print("Maximum Heart Rate is " + str(round(max_heart_rate,2)))
print("Target Heart Rate (Higher) is " + str(round(target_heart_rate_higher,2)))
print("Target Heart Rate (Lower) is " + str(round(target_heart_rate_lower,2)))
