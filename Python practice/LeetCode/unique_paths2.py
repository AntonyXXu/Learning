# https://leetcode.com/problems/unique-paths-ii/

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid:
        return 0
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    if obstacleGrid[rows-1][cols-1] == 1:
        return 0
    if obstacleGrid[0][0] == 1:
        return 0
    if rows == 1 and cols == 1 and obstacleGrid[0][0] == 0:
        return 1

    val = 1
    for i in range(1, rows):
        if obstacleGrid[i][0] == 1:
            val = 0
        obstacleGrid[i][0] = val
    val = 1
    for j in range(1, cols):
        if obstacleGrid[0][j] == 1:
            val = 0
        obstacleGrid[0][j] = val

    for row in range(1, rows):
        for col in range(1, cols):
            value = obstacleGrid[row-1][col] + obstacleGrid[row][col-1]
            if obstacleGrid[row][col] == 1:
                value = 0
            obstacleGrid[row][col] = value

    return obstacleGrid[rows-1][cols-1]

print(uniquePathsWithObstacles(   [[0,0,0],[0,1,0],[0,0,0]]  ))
print(uniquePathsWithObstacles(  [[0,1],[0,0]]   ))
print(uniquePathsWithObstacles(  [[0]]   ))