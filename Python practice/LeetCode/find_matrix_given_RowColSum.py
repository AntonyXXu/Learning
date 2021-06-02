rowSum = [3,8]
colSum = [4,7]
rowSum1 = [5,7,10] 
colSum1 = [8,6,8]

def matrix(rowSum, colSum):
    if len(rowSum) == 0:
        return colSum
    if colSum == 0:
        return rowSum
    res = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
    row = 0
    col = 0
    while row < len(rowSum) and col < len(colSum) :
        if rowSum[row] < colSum[col]:
            res[row][col] = rowSum[row]
            colSum[col] -= rowSum[row]
            rowSum[row] = 0
            
        elif colSum[col] < rowSum[row]:
            res[row][col] = colSum[col]
            rowSum[row] -= colSum[col]
            colSum[col] = 0
            
        else:
            res[row][col] = rowSum[row]
            rowSum[row] = 0
            colSum[col] = 0
        if rowSum[row] == 0:
            row += 1
        if colSum[col] == 0:
            col += 1           
    return res

print(matrix(rowSum, colSum))
print(matrix(rowSum1, colSum1))