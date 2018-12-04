"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
# function to check if a string is pangram or not
def pangram(input_string):
    count = 0
    _list = []
    _lower = input_string.lower()
    for alpha in _lower:
        _list.append(alpha)
    # remove duplicates by using set() function
    _noDupli = set(_list)
    for elements in _noDupli:
        if elements in 'abcdefghijklmnopqrstuvwxyz':
            count += 1
        else:
            pass
    if count == 26:
        print ("Pangram")
    else:
        print ("Not Pangram")
    
pangram(input("Enter the string :"))