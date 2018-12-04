"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format4.py
  Problem Statement:
    This program accepts the user’s first name and last name 
    Print them in reverse order with a space between them.
    Take Input from User 
    Your code should have only a single user input statement.  
  Hint:
    Try to serach for some function in the str using help() and dir()
  Input:
    Forsk Technologies
  Output:
    Technologies Forsk
"""

# input string
user_input = input("Enter a string :")

# string after using splt function
splitted_string = user_input.split()

# reverse splitted string
reverse_splitted_string = splitted_string[::-1]

# Output 
print (" ".join(reverse_splitted_string))