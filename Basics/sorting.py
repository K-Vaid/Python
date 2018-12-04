# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:27:27 2018

@author: Kunal Vaid

Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, score) tuples
    by ascending order where name is string, age and score are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), 
    ('Tom', 19, 80)]
"""

user_input = input("Enter name, age and score: ")

# separating individual student record from the input
student_list = user_input.split("\n")

# separating individual value for each student in student list
student_list = map(lambda i: i.split(","),student_list)

sorted_student_list = []

for student in student_list:
    student_tuple = []
    
    for value in student:
        if value.isdigit():
            student_tuple.append(int(value))
        else:
            student_tuple.append(value.strip())
    
    sorted_student_list.append(tuple(student_tuple))


sorted_student_list.sort()
print (sorted_student_list)