"""
Code Challenge
  Name: 
    Age Calculator
  Filename: 
    age_cal.py
  Problem Statement:
    Lets assume your age is 21 today
    What would be your age after 5 years from today 
    How old were you 10 years back
  Hint: 
    You need to add to calculate future age 
    You need to subtract to calculate your past age 
"""

# Enter your age
user_age = int(input("Enter your age :"))

# Enter years after that you want to calculate your age
f_years = int(input("Enter the no. of years after, to calculate your age :"))

# Enter years before that you want to calculate your age
p_years = int(input("Enter the no. of years back, to calculate your age :"))

future_age = user_age + f_years

past_age = user_age - p_years

print ("Your current age is : {0}".format(user_age))

print ("Your age after {0} years will be : {1}".format(f_years,future_age))

print ("Your age before {0} years was : {1}".format(p_years,past_age))