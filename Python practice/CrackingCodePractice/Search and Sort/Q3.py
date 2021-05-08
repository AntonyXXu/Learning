#Search in rotated sorted array
x = [5,6,7,9,-4,3,4]
x = [2,2,2,3,4,2]

def findPivot(arr, low, high):
    if low >= high:
        return low
    index = (low+high)//2
    if index < 1 or index >= len(arr)-1:
        return 0
    if arr[index] > arr[index+1]:
        return index+1
    if arr[index-1] > arr[index]:
        return index
    if arr[index] > arr[0]:
        return findPivot(arr, index+1, high)
    else:
        return findPivot(arr, low, index-1)

def findVal(arr, val):
    if len(arr) < 1:
        return -1
    piv = findPivot(x, 0, len(arr)-1)
    i = 0
    j = len(arr)-1
    if val == arr[piv]:
        return piv
    if val >= arr[piv] and val <= arr[len(arr)-1]:
        i = piv+1
    else:
        j = piv-1
    while i <= j:
        mid = (i + j) // 2
        if arr[mid] == val:
            return mid
        if val < arr[mid]:
            j = mid - 1
        else: 
            i = mid + 1       
    return -1

print(findVal(x, 3))
print(findVal([1],1))