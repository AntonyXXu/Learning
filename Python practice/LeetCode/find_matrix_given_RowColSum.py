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
    while row < len(rowSum) and rowSum[row] > 0:
        while col < len(colSum) and colSum[col] > 0 :
            if rowSum[row] <= colSum[col]:
                res[row][col] = rowSum[row]
                rowSum[row] = 0
                row += 1
            else:
                res[row][col] = colSum[col]
                colSum[col] = 0
                col += 1
            if row >= len(rowSum) and row >= len(colSum):
                return res
        row += 1
    return res

print(matrix(rowSum, colSum))
print(matrix(rowSum1, colSum1))