"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    noraml_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

# Include required libraries

# numpy library 
import numpy as np

# matplotlib library for visualization
import matplotlib.pyplot as plt

# Create a normally distributed random data
random_data = np.random.normal(loc=150, scale=20, size=1000)

# plot histogram
plt.hist(random_data, bins=100)
plt.show()

# Calculate Standard Deviation
standard_deviation = np.std(random_data)

# Calculate Variance
variance = np.var(random_data)

print ("Standard Deviation : "+str(round(standard_deviation,2)))

print ("Variance : "+str(round(variance,2)))
