# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:18:11 2021

@author: Test
"""

#Exceptions
try:
    print("raising exception:")
    raise Exception('abc','123')
except Exception as instance:
    print(instance.args)
    x,y = instance.args
    print("x = ",x,"\ny = ",y)
    
def conversion(x):
    assert (x>=0), "x is negative"
    print(x**2)

conversion(20)
conversion(-5)