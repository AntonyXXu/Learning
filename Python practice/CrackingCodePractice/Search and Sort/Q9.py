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

def search2(matrix, val):
    if matrix == None or val == None:
        return [-1, -1]
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        x = matrix[row][col]
        if matrix[row][col] == val:
            return [row, col]
        if matrix[row][col] > val:
            col -= 1
        else:
            row += 1
    return [-1,-1]

print(search2(matrix1, target1))       
print(search2(matrix, target))

