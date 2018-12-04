"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
    Take the number from the keyboard as input from the user.
  Hint: 
    Factorial of 3 = 3  2  1= 6 
    Try to first find the function from math module using dir and help 
"""

from math import factorial

input_number = input("Enter the number :")
Factorial_of_input_number = factorial(input_number)

print ("Factorial of {0} is {1}".format(input_number,Factorial_of_input_number))