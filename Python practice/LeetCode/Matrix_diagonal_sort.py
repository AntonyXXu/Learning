# A matrix diagonal is a diagonal line of cells starting from some cell in either the 
# topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. 
# For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

def diagSort(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    temp = []
    for row in range(rows):
        r = row
        col = 0
        while col < cols and r < rows:
            temp.append(matrix[r][col])
            col += 1
            r += 1
        temp.sort(reverse = True)
        r = row
        col = 0
        while col < cols and r < rows:
            matrix[r][col] = temp.pop()
            col += 1
            r += 1
    for col in range(1, cols):
        c = col
        row = 0
        while row < rows and c < cols:
            temp.append(matrix[row][c])
            row += 1
            c += 1
        temp.sort(reverse=True)
        c = col
        row = 0
        while len(temp):
            matrix[row][c] = temp.pop()
            row += 1
            c += 1
    return matrix

mat1 = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(diagSort(mat1))

mat2 = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
res2 = [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
print(diagSort(mat2))
assert(diagSort(mat2) == res2)