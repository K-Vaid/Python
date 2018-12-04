"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
      RESTART
  Output: 
      RESTA$T
"""

input_string = raw_input("Enter your String :")

replaced_char = raw_input("Enter Character which you want to replace :")

replacement_char = raw_input("Enter Character using which you want to replace :")

# First occurence of replaced character
first_occurence = input_string.find(replaced_char)

# Replace replaced character with replacement character from input string
inp2_str = input_string.replace(replaced_char, replacement_char)

# Convert into list
inp2_str = list(inp2_str)

# Remove replacement character from first occurrence
inp2_str.remove(replacement_char)

# Insert replaced character on it's first occurrence again
inp2_str.insert(first_occurence, replaced_char)

# now join to make Final string
inp2_str = ''.join(inp2_str)

print("Final String is "+inp2_str)