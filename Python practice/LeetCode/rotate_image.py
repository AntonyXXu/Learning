# https://leetcode.com/problems/rotate-image/

def rotate(matrix):
    rows = len(matrix) 
    cols = len(matrix[0]) 
    for row in range(rows//2 + rows%2):
        for col in range(cols//2):
            temp = matrix[row][col]
            matrix[row][col] = matrix[rows - col - 1][row]
            matrix[rows - col - 1][row] = matrix[rows - row - 1][cols - col - 1]
            matrix[rows - row - 1][cols - col - 1] = matrix[col][cols - row - 1]
            matrix[col][cols - row - 1] = temp
    print(matrix)
    return matrix

print(rotate(  [[1]]) == [[1]])
print(rotate( [[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]])
print(rotate( [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] )
