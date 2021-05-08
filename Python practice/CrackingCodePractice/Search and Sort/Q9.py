#Matrix Search, each row and column is ascending

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3

def binarySearch(arr, low, high, val):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == val:
        return mid
    if val < arr[mid]:
        return binarySearch(arr, low, mid-1, val)
    else:
        return binarySearch(arr, mid+1, high, val)

def search(matrix, val):
    for i in range(len(matrix)):
        res = binarySearch(matrix[i], matrix[i][0], len(matrix[i])-1, val)
        if res != -1:
            return [i,res]
    return [-1, -1]
        
print(search(matrix, target))
print(search(matrix1, target1))


