# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:18:22 2021

@author: Test
"""
#%%



def max_wealth(accounts):
    maximum = 0
    for element in accounts:
         maximum = max(sum(element),maximum)
    return maximum
    
x=[[1,2],[2,3]]
u=[[1,5],[7,3],[3,5]]
y=[[1,2,3],[3,2,1]]
z=[[2,8,7],[7,1,3],[1,9,5]]

print(max_wealth(u))
