# https://leetcode.com/problems/triangle/

def minTotal(triangle):
    if not triangle:
        return 0
    rows = len(triangle)
    for row in range(1, rows):
        cols = len(triangle[row])
        for col in range(cols):
            if col == 0:
                triangle[row][col] = triangle[row-1][col] + triangle[row][col]
            elif col == cols - 1:
                triangle[row][col] = triangle[row-1][col-1] + triangle[row][col]
            else:
                triangle[row][col] = min(triangle[row-1][col-1],triangle[row-1][col])+ triangle[row][col]
    return min(triangle[-1])

print(minTotal( [[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minTotal( [[-10]] ))