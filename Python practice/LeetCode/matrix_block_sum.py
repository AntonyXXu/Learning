# https://leetcode.com/problems/matrix-block-sum/
m1 = [[1,2,3],[4,5,6],[7,8,9]]
k1 = 1
k2 = 2

def matrix_block_sum(m,k):
    if not m:
        return None
    if k == 0:
        return m
    rows = len(m)
    cols = len(m[0])
    rangeSum = [[0 for row in range(rows)] for col in range(cols)]
    for row in range(rows):
        rowSum = 0
        for col in range(cols):
            rowSum += m[row][col]
            rangeSum[row][col] += rowSum
            if row > 0:
                rangeSum[row][col] += rangeSum[row-1][col]
    res = [[0 for row in range(rows)] for col in range(cols)]
    for row in range(rows):
        for col in range(cols):
            rmin = row - k if row - k > 0 else 0
            cmin = col - k if col - k > 0 else 0
            rmax = row + k if row + k < rows-1 else rows-1
            cmax = col + k if col + k < cols-1 else cols-1
            num = rangeSum[rmax][cmax]
            if rmin > 0:
                num -= rangeSum[rmin-1][cmax]
            if cmin > 0:
                num -= rangeSum[rmax][cmin-1]
            if rmin > 0 and cmin > 0:
                num += rangeSum[rmin-1][cmin-1]
            res[row][col] = num


    return res

print(matrix_block_sum(m1, k1))
print(matrix_block_sum(m1, k2))

    
