"""
Code Challenge
  Name: 
    Area and Perimeter of Circle
  Filename: 
    circle.py
  Problem Statement:
    Take the radius of the circle from the keyboard as input from the user 
    Calculate the area and perimeter of it.
  Hint: 
    Pi  radius  radius is the area of circle
    2  Pi  radius is the perimeter of circle 
    Use math module to get the value of Pi ( 3.14 ) 
"""

from math import pi

radius_of_circle = input("Enter radius of circle :")

area_of_circle = pi*(radius_of_circle**2)

perimeter_of_circle = 2*pi*radius_of_circle

print ("Area of Circle is "+str(area_of_circle))

print ("Perimeter of Circle is "+str(perimeter_of_circle))
