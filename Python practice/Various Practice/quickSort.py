arr = [12, 11, 6, -1, 0, -7, 5, -3, -6, -7, 12]

def quickSort(arr, low = 0, high = len(arr) - 1):
    if low >= high:
        return arr
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot - 1)
    quickSort(arr, pivot+1, high)

def partition(arr, low, high):
    pivot = low
    pivotVal = arr[low]
    ptr1 = low+1
    ptr2 = high
    done = False
    while not done:
        while ptr1 <= ptr2 and pivotVal >= arr[ptr1]:
            ptr1 += 1 
        while ptr1 <= ptr2 and pivotVal <= arr[ptr2]:
            ptr2 -= 1
        if ptr2 > ptr1:
            arr[ptr1], arr[ptr2] = arr[ptr2], arr[ptr1]
        else: 
            done = True
    arr[pivot] = arr[ptr2]
    arr[ptr2] = pivotVal
    return ptr2

middle val

def quickSort(arr, low = 0, high = len(arr)-1):
    if low >= high:
        return
    pivot = partition(arr, low, high)
    quickSort(arr, low, pivot-1)
    quickSort(arr, pivot+1, high)

def partition(arr, low, high):
    #swap to middle
    pivot = (low+high)//2
    arr[low], arr[pivot] = arr[pivot], arr[low]
    piv_val = arr[low]
    i = low + 1
    j = high
    while i < j:
        while i <= j and piv_val >= arr[i]:
            i+=1
        while piv_val < arr[j]:
            j-=1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j],arr[low]
    return j

quickSort(arr)
#quickSort(arr)
print(arr)
