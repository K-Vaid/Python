"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format.py
  Problem Statement:
    This program prints out the following string in a specific format (see the output). 
  Hint: 
    The string should be printed using a single print statement only and the indexes shouldn't be counted manually.
  Input:
    mystr ='''
    This is a multi line string. This code challenge is to
    test your understanding about strings.
    You need to print some part of this string.
    From here print this text without manually counting the indexes.'''
  Output:
    From here print this text without manually counting the indexes.
"""

input_string = """This is a multi line string. This code challenge is to
test your understanding about strings.You need to print some part of this string.
From here print this text without manually counting the indexes."""

# Find index from we want to start print input string
index = input_string.find("From here")

# output string
output_string = input_string[index:]

print ("Output string is : "+output_string)