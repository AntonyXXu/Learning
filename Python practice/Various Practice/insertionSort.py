#insertion sort

arr = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
x = [3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

def insertionsort(data):
    for index in range(1,len(data)):
        temp = data[index]
        pos = index
        while pos > 0 and data[pos-1]>temp:
            data[pos] = data[pos-1]
            pos = pos - 1
        data[pos] = temp
    return data

y = insertionsort([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
print(y)      

def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1]>temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr


print(insertionSort(x))
print(x)