def pattern(arr, m, k):
    if k == 0 or m == 0:
        return True
    if len(arr) == 1 and m == 1 and k == 1:
        return True
    contiguous = 1
    for i in range(len(arr) - m):
        if arr[i] == arr[i + m]:
            contiguous += 1
        else:
            contiguous = 1
        if contiguous == (k) * m:
            return True
    return False

arr = [1,2,4,4,4,4]
m = 1
k = 3

print(pattern(arr,m,k))

print(pattern(arr = [1,2,1,1,1,2,1,3], m = 2, k = 2))