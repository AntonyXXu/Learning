# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:13:13 2021

@author: Test
"""

#selectionsort
def selectionsort(data):
    for index in range(len(data)):
        small = index
        temp = data[index]
        for i in range(index,len(data)):
            if data[i] < data[small]:
                small = i
        data[index] = data[small]
        data[small] = temp
    return data
        
x = selectionsort([2,4,5,1,3])
print(x)

#%% insertion sort
def insertionsort(data):
    for index in range(1,len(data)):
        temp = data[index]
        pos = index
        while pos > 0 and data[pos-1]>temp:
            data[pos] = data[pos-1]
            pos = pos - 1
        data[pos] = temp
    return data

y = insertionsort([2,4,5,1,3])
print(y)      

#%% merge sort
def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else: 
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

x = merge([1,3,5],[2,4,6,8])
print(x)

def mergesort(data):
    if len(data)<=1:
        return data
    middle = len(data)//2
    left = mergesort(data[:middle])
    right = mergesort(data[middle:])
    return merge(left,right)

y = mergesort([1,9,5,7,6,3,2,5,8,0])
print(sorted([1,9,5,7,6,3,2,5,8,0]))
print(y)

#%% quick sort
def quicksort_help(data,first,last):
    if first < last:
        pivot = partition(data,first,last)
        quicksort_help(data,first,pivot-1)
        quicksort_help(data,pivot+1,last)

def partition(data,first,last):
    pivotval = data[(first - last)//2]
    left = first+1
    right = last
    complete = False
    while not complete:
        while left <= right and data[left]<=pivotval:
            left +=1
        while right >= left and data[right]>= pivotval:
            right +=1
        if right < left:
            complete = True
        else: 
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
    temp = data[first]
    data[first] = data[right]
    data[right] = temp
    return right

def quicksort(data):
    return quicksort_help(data,0,len(data)-1)

y = mergesort([1,9,5,7,6,3,2,5,8,0])
print(y)
