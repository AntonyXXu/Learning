# https://leetcode.com/problems/spiral-matrix/

def spiralOrder(matrix):
    if not matrix:
        return []
    left = 0
    top = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    r = 0
    c = 0
    ans = []
    while left <= right and top <= bottom:
        for c in range(left, right + 1):
            ans.append(matrix[r][c])
        top += 1
        for r in range(top, bottom + 1):
            ans.append(matrix[r][c])
        right -= 1
        if top <= bottom:
            for c in range(right, left -1, -1):
                ans.append(matrix[r][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                ans.append(matrix[r][c])
            left += 1
        
    return ans
        

print(spiralOrder( matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder( matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))