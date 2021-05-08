#Matrix Search, each row and column is ascending, each row is larger than the prev

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 13

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3

def search(matrix, val):
    row = 0
    col = 0
    low = 0
    high = len(matrix[0]) * len(matrix)
    maxC = len(matrix[0]) - 1
    while  low <= high:
        mid = (high + low) // 2
        row = mid // len(matrix[0])
        col = mid % len(matrix[0])
        midV = matrix[row][col]
        if midV == val:
            return [row, col]
        if val < midV:
            high = mid - 1
        else:
            low = mid + 1

    return [-1,-1]

print(search(matrix,target))
print(search(matrix1,target1))
print(search(matrix1,-10))