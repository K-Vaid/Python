# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:53:23 2018

@author: Kunal vaid

# Hands On 2
# Make a function days_in_month to return the number of days
# in a specific month of a year
"""

days_30 = {4:"Apr",6:"Jun",9:"Sept",11:"Nov"}

def days_in_month(month,year):
    # check if the Month has 30 days
    if month in days_30:
        return 30
    else:
        # Check for Feb
        if month == 2:
            # Check for leap year
            if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
                return 29
        else:
            # For the remaining months that has 31 days
            return 31
    # if non of the above is true then no. of days of Feb (without leap year)
    return 28

inp_month = int(input("Enter Month (like 1 for Jan, 2 for Feb...): "))
inp_year = int(input("Enter Year: "))

print ("\nNumber of days in {0}/{1} is: {2}".format(str(inp_month),
       str(inp_year),str(days_in_month(inp_month,inp_year))))



########## Pythonic Code ##########
'''
from calendar import monthrange
print ("\nNumber of days in {0}/{1} is: {2}".format(str(inp_month),
       str(inp_year),str(monthrange(inp_year, inp_month)[1])))'''