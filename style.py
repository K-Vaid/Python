"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert uppercase characters to lowercase 
    Lowercase characters to uppercase ( swap case ) for the name. 
    Take this name as input from the keyboard. 
    Also convert the inputed string in CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str and see its help on how to use it. 
"""

input_string = input("Enter your string :")

camel_case_string = input_string.title()

upper_case_string = camel_case_string.upper()

lower_case_string = camel_case_string.lower()

print("Camel Case string is "+camel_case_string)

print("Upper Case string is "+upper_case_string)

print("Lower Case string is "+lower_case_string)