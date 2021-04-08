x = [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
y = [3, 4, 5, 6, 7, 8, 0]
test = sorted(x)

def binarySearch(arr, val, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == val:
        return mid
    if val < arr[mid]:
        return binarySearch(arr, val, low, mid - 1)
    if val > arr[mid]:
        return binarySearch(arr, val, mid + 1, high)

def findPivot(arr):
    if len(arr) == 1:
        return 0
    return findPivotHelper(arr, 0, len(arr)-1)

def findPivotHelper(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] > arr[mid+1]:
        return mid + 1
    elif arr[mid - 1] > arr[mid]:
        return mid
    elif arr[mid] < arr[low]:
        return findPivotHelper(arr, low, mid - 1)
    else:
        return findPivotHelper(arr, mid+1, high)

def find(arr, val):
    piv = findPivot(arr)
    n = len(arr)
    if arr[piv] == val:
        return piv
    elif piv == 0:
        return binarySearch(arr, val, 0, n - 1 )
    elif val >= arr[0]:
        return binarySearch(arr, val, 0, piv - 1)
    else:
        return binarySearch(arr, val, piv, n-1)

