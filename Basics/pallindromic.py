"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, then you need to print True else print False.
    (Take Input from User)  
  Hint: What is pallindromic Integer 
  Input: 
    12 9 61 5 14
  Output:
    True
"""

# give list of inputs from user
user_input = input("Enter space seperated values :").split()

if all([int(i)>0 for i in user_input]) and any([i==i[::-1] for i in user_input]):
    print ("True")
else:
    print ("False")
    