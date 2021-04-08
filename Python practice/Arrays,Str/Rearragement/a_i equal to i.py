#Rearrange an array such that arr[i] = i

arr = [-10, 10, 6, 1, 9,
        3, 2, -1, 4, -1]
def fix(arr):
    length = len(arr)
    if not arr:
        return False
    for i in range(length):
        if arr[i] >= length or arr[i] < 0:
            arr[i] = -1
        else:
            while arr[i] != i and arr[i] != -1:
                newIndex = arr[i]
                temp = arr[newIndex]
                arr[newIndex] = arr[i]
                arr[i] = temp
                if arr[i] >= length:
                    arr[i] = -1
    return True

fix(arr)
print(arr)