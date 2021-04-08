#binary search for a rotated array

x = [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
y = [3, 4, 5, 6, 7, 8, 0]
def findPivot(arr, first, last):
    if first > last:
        return -1
    if arr[last] > arr[first]:
        return first
    mid = (first + last) // 2
    if arr[mid-1] > arr[mid]:
        return mid
    if arr[mid] > arr[mid+1]:
        return mid+1
    if arr[first] > arr[mid]:
        return findPivot(arr, first, mid - 1) 
    else:
        return findPivot(arr, mid+1, last)

def findPivotIt(arr):
    low = 0
    high = len(arr)-1
    while high > low:
        if arr[low] < arr[high]:
            return low
        mid = (high + low) // 2
        if arr[mid] > arr[mid+1]:
            return mid+1
        if arr[mid-1] > arr[mid]:
            return mid
        if arr[low] < arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

print(findPivot(y, 0, len(y)-1))
print(findPivotIt(y))

def binarySearch(arr, val, high, low):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return mid
        if val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def find(arr, val):
    piv = findPivotIt(arr)
    high = len(arr) - 1
    low = 0
    if piv == 0:
        return binarySearch(arr, val, high, low)
    if val >= arr[low]:
        return binarySearch(arr, val, piv - 1, low)
    if val <= arr[high]:
        return binarySearch(arr, val, high, piv)
    else:
        print("lalala")

