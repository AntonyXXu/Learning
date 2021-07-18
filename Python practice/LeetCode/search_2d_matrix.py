# https://leetcode.com/problems/search-a-2d-matrix/

def searchMatrix(matrix, target):
    if not matrix:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    length = rows * cols
    left = 0
    right = length - 1
    while left <= right:
        mid = (left + right) // 2
        if mid < 0 or mid > length:
            return False
        row = (mid )// cols
        col = (mid) % cols
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            right = mid - 1
        else:
            left = mid + 1
        
    return False

print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))