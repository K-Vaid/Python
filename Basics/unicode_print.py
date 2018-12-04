#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:07:51 2018

@author: dev
"""

"""

Code Challenge
  Name: 
    Unicode Printing
  Filename: 
    unicode_print.py
  Problem Statement:
    Print the below string as it is   
    UNIX® and Sun Microsystem™ are  ©, 2018 Oracle
  Hint: 
     Use unicode \u00AE for Registered ® 
     Use unicode \u00A9 for Copyright © 
     use unicode \u2122 for TradeMark ™ 
  Output:
     UNIX® and Sun Microsystem™ are  ©, 2018 Oracle



"""
print ("UNIX"+u"\u00AE and Sun Microsystem"+u"\u2122 are"+" "+u"\u00A9"+", 2018 Oracle")
