#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:56:11 2018

@author: dev
"""

"""

Code Challenge
  Name: 
    Name Printing in English
  Filename: 
    name_english.py
  Problem Statement:
    Print your First Name and Last Name in Quotation. 
    Both the first name and Last name should be on different lines 
  Hint: 
     Use the Escape Code for quotation and new line
  Output:
    "Sylvester"
    "Fernandes"

"""

first_name,last_name = input("Enter your name with last name :").split(" ")

print (str("\""+first_name+"\""+"\n"+"\""+last_name+"\""))