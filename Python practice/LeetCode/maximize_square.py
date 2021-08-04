# https://leetcode.com/problems/maximal-square/

def maximalSquare(matrix):
    if not matrix:
        return 0
    ans = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            if row > 0 and col > 0:
                if matrix[row][col] == "1":
                    matrix[row][col] = min(
                        int(matrix[row-1][col]),
                        int(matrix[row][col-1]),
                        int(matrix[row-1][col-1]),
                    ) + int(matrix[row][col])

            ans = max(int(matrix[row][col]), ans)
    return ans ** 2


print(maximalSquare(matrix=[["1", "0", "1", "0", "0"], [
      "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(maximalSquare(matrix=[["0", "1"], ["1", "0"]]))
print(maximalSquare(matrix=[["0"]]))
print(maximalSquare(matrix=[["1"]]))
print(maximalSquare([["1", "0", "1", "0"], ["1", "0", "1", "1"], [
      "1", "0", "1", "1"], ["1", "1", "1", "1"]]))
print(maximalSquare(
    [["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["0", "0", "1", "1", "1"]]))
print(maximalSquare(
    [["1", "0", "1", "1", "0", "1"], ["1", "1", "1", "1", "1", "1"], ["0", "1", "1", "0", "1", "1"], ["1", "1", "1", "0", "1", "0"], ["0", "1", "1", "1", "1", "1"], ["1", "1", "0", "1", "1", "1"]]))
