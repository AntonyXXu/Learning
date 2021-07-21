# https://leetcode.com/problems/out-of-boundary-paths/

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    if maxMove == 0:
        return 0
    if startRow < 0 or startColumn < 0 or startRow >= m or startColumn >= n:
        return 0
    ans = (findPaths(m, n, maxMove - 1, startRow -1, startColumn) +
        findPaths(m, n, maxMove - 1, startRow, startColumn - 1) +
        findPaths(m, n, maxMove - 1, startRow + 1, startColumn ) +
        findPaths(m, n, maxMove - 1, startRow, startColumn + 1))
    if startRow == 0:
        ans += 1
    if startRow == m - 1:
        ans += 1
    if startColumn == n - 1:
        ans += 1
    if startColumn == 0:
        ans += 1
    return ans%1000000007

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    if maxMove == 0:
        return 0
    if m == 1 and n == 1:
        return 4
    odd = [[0 for _ in range(n)] for _ in range(m)]
    even = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(maxMove):
        if i % 2 == 0:
            dpPrev = odd
            dpCurr = even
        else:
            dpPrev = even
            dpCurr = odd
        for row in range(m):
            for col in range(n):
                num = 0
                if row > 0:
                    num += dpPrev[row-1][col]
                else:
                    num += 1
                if col > 0:
                    num += dpPrev[row][col-1]
                else:
                    num += 1
                if row < m-1:
                    num += dpPrev[row+1][col]
                else:
                    num += 1
                if col < n-1:
                    num += dpPrev[row][col+1]
                else:
                    num += 1
                dpCurr[row][col] = num
        ans = dpCurr[startRow][startColumn]
    return ans%1000000007


    

print(findPaths(2, 2, 2, 0, 0))
print(findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
