"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""


def make_bricks(small, big, goal):
    if goal % 5 > small:
        print (False) 
    else:    
        c = big*5 + small
        if c >= goal:
            print (True)
        else:
            print (False)

lst = list(map(int,input("Enter Numbers: ").split(",")))
make_bricks(lst[0], lst[1], lst[2])