def zeroMatrix(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    col_zero = cols*[False]
    row_zero = rows*[False]
    for i in range(cols):
        for j in range(rows):
            if matrix[i][j] == 0:
                col_zero[i] = True
                row_zero[j] = True
    for i in range(cols):
        for j in range(rows):
            if col_zero[i] or row_zero[j]:
                matrix[i][j] = 0

def zeroMatrix2(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    for i in range(cols):
        for j in range(rows):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    for i in range(1, cols):
        for j in range(1, rows):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

matrix1 = [[0,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,0,6],[7,8,9]]
matrix3 = [[1,2,3],[4,5,6],[7,8,0]]

zeroMatrix2(matrix1)
zeroMatrix2(matrix2)
zeroMatrix2(matrix3)
print(matrix1)
print(matrix2)
print(matrix3)