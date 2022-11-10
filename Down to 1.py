# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 22:30:48 2022

@author: Jon


Write a Python module that computes the number of steps required for the sequence to get 'down to 1.'

Given any positive integer, n at each step do this:

   If n is odd replace n with 3*n+1

  if n is even, replace n with n/2

for example if n =11 the the sequence is  11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 .... it took 14 steps

print out the number of steps required for the integers 5 through 20

"""

count = []

for x in range(5,21):
    counter = 0
    while x != 1:
        if (x % 2) == 0:
            x = x/2 
            print(x) 
            counter += 1
            
        elif (x % 2) != 0:
            x = 3*x+1
            print(x)
            counter += 1
    print("This took", counter, "steps."),
    count.append(counter)
print(count)
