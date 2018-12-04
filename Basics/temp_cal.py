"""
Code Challenge
  Name: 
    Temperature Calculator
  Filename: 
    temp_cal.py
  Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it.
  Hint: 
    Multiply by 9/5 and add 32  to get in Fahrenheit
    Add 273 approximately to get in Kelvin
"""

# Enter temperature in degree Centigrade
temp_c = float(input("Enter today's city temperature in degree centigrade :"))

# temperature in degree fahrenheit
temp_f = ((9/5.0)*temp_c)+32

# temperature in degree kelvin
temp_k = (temp_c+273)

print ("Today's temperature in degree centigrade :"+str(temp_c))

print ("Today's temperature in degree fahrenheit :"+str(temp_f))

print ("Today's temperature in degree kelvin :"+str(temp_k))