# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:18:16 2021

@author: Test
"""

#%% Sequential Search

def seqsearch(dataset,key):
    index = 0
    found = False
    while not found and index < len(dataset):
        if dataset[index] == key:
            found = True
        else:
            index += 1
    if not found:
        index = -1
    return index

a = [1,2,3,4,5,6,7,8,9,10]
b = 8
c = 11
print(seqsearch(a,b))
print(seqsearch(a,c))

#%% Binary Search

def BinarySearch(dataset,key):
    low = 0
    high = len(dataset)-1
    found = False
    while not found and low <= high:
        mid = (low+high)//2
        if dataset[mid] == key:
            found = True
        elif dataset[mid] < key:
            low = mid + 1
        elif dataset[mid] > key:
            high = mid - 1
    if not found: 
        mid = -1
    return mid

    
a = [1,2,3,4,5,6,7,8,9,10]
b = 8
c = 11

print(BinarySearch(a,b))
print(BinarySearch(a,c))

#%% Interpolation Search
def interpolationSearch(dataset,key):
    low = 0
    high = len(dataset)-1
    found = False
    while not found and low < high :
        guess = low + (key - dataset[low])*(high - low) // (dataset[high] - dataset[low])
        if guess > (len(dataset)-1) or guess>high or guess<low :
            break
        elif dataset[guess] == key:
            found = True
        elif dataset[guess] < key:
            low = guess + 1
        else:
            high = guess - 1
    if not found:
        guess = -1
    return guess

    
    
a = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
print(a)
b = 20
c = 60
d = 46
print(interpolationSearch(a,b))
print(interpolationSearch(a,c))
print(interpolationSearch(a,d))

#%%
#Exponential Search
def BinarySearch(dataset,key):
    low = 0
    high = len(dataset)-1
    found = False
    while not found and low <= high:
        mid = (low+high)//2
        if dataset[mid] == key:
            found = True
        elif dataset[mid] < key:
            low = mid + 1
        elif dataset[mid] > key:
            high = mid - 1
    if not found: 
        mid = -1
    return mid

def exponentialSearch(dataset,key):
    if dataset[0] == key:
        return 0
    found = False
    guess = 1
    while not found and guess <= len(dataset)-1 and dataset[guess]<=key:
        if dataset[guess] == key:
            return guess
        else:
            guess = guess*2
    return BinarySearch(dataset[:min(guess,len(dataset)-1)], key)
        
    
a = [2, 3, 6, 8, 16, 33, 68,
       130, 254, 513, 1080, 2049, 4095, 8195, 16385]
print(a)
b = 1080
c = 1700
d = 16385
print(interpolationSearch(a,b))
print(interpolationSearch(a,c))
print(interpolationSearch(a,d))