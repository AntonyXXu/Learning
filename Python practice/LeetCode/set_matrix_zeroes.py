# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    if not matrix:
        return matrix
    first = False
    if matrix[0][0] == 0:
        first = True
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0
    
    for row in range(1, rows):
        if matrix[row][0] == 0:
            for col in range(cols):
                matrix[row][col] = 0


    for col in range(1, cols):
        if matrix[0][col] == 0:
            for row in range(rows):
                matrix[row][col] = 0

    if first:
        for row in range(rows):
            matrix[row][0] = 0
        for col in range(cols):
            matrix[0][col] = 0
    
    return matrix


print(setZeroes(    [[1,1,1],[1,0,1],[1,1,1]]  ) ==[[1,0,1],[0,0,0],[1,0,1]] )
print(setZeroes(   [[0,1,2,0],[3,4,5,2],[1,3,1,5]]    ) ==[[0,0,0,0],[0,4,5,0],[0,3,1,0]])
