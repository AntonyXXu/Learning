# https://leetcode.com/problems/minimum-path-sum/

def minPathSum(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(1, rows):
        grid[row][0] += grid[row-1][0]
    for col in range(1, cols):
        grid[0][col] += grid[0][col-1]
    for row in range(1, rows):
        for col in range(1, cols):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    return grid[rows-1][cols-1]

print(minPathSum( [[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum( [[1,2,3],[4,5,6]]))
