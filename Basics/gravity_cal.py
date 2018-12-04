"""
Code Challenge
  Name: 
    Gravity Calculator
  Filename: 
    gravity_cal.py
  Problem Statement:
    Compute the position of the object after falling for 10 seconds. 
    Output the value meters and assume that the acceleration is -9.81  
  Hint: 
    Distance = (Acceleration*Time*Time ) / 2
"""

# Falling time in seconds
falling_time = int(input("Enter time in seconds of falling object: "))

# Acceleration value
acceleration = -9.81

# Distance travel by object
distance = abs((acceleration*falling_time*falling_time) / 2)

print ("Distance covered by object after falling for {0} seconds : {1} meters".format(falling_time, distance))