
"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(s):
  consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
  trans = ''.join(i + 'o' + i if i in consonants else i for i in s)
  print (trans)

name = input("enter: ")
# translate(m)
translate(name)