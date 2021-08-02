# https://leetcode.com/problems/number-of-islands/

def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    ans = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                ans += 1
                mark(grid, row, col)
    return ans


def mark(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
        return
    grid[row][col] = '0'
    mark(grid, row+1, col)
    mark(grid, row-1, col)
    mark(grid, row, col+1)
    mark(grid, row, col-1)


print(numIslands(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
