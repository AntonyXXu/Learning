# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:45:45 2021

@author: Test
"""

#%% factorial
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
    

print(factorial(2))
