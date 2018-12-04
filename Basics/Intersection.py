# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:53:42 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above
    given lists.  
"""

first_list = [1,3,6,78,35,55]

second_list = [12,24,35,24,88,120,155]

# Using set to get the intersection of first and second list
intersection_list = list(set(first_list) & set(second_list))

print (intersection_list)