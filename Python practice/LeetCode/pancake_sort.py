# https://leetcode.com/problems/pancake-sorting/

def pancakeSort(arr):
    res = []
    for i in range(len(arr)):
        m = getMax(arr[:len(arr)-i])
        if m != len(arr) - i - 1:
            rev(arr, m+1)
            res.append(m+1)
            rev(arr, len(arr)-i)
            res.append(len(arr)-i)
    return res

def rev(arr, n):
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

def getMax(arr):
    m = 0
    for i in range(len(arr)):
        if arr[m] < arr[i]:
            m = i
    return m

print(pancakeSort([3,2,4,6,5,1]))
print(pancakeSort([3,2,4,1]))
print(pancakeSort([1,2,3]))