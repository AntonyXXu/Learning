# Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix of integers in the constructor and supports two methods:

# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)

# Updates all values with newValue in the subrectangle whose upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).
# 2. getValue(int row, int col)

# Returns the current value of the coordinate (row,col) from the rectangle.

class Rect:
    def __init__(self, arr):
        self._arr = arr
        self._maxR = len(arr)
        self._maxC = len(arr[0])

    def getValue(self, row, col):
        return self._arr[row][col]
    
    def updateSubRectangle(self, row1, col1, row2, col2, newVal):
        if 0 > row1 or row1 > row2 or row2 > self._maxR\
            or 0 > col1 or col1 > col2 or col2 > self._maxC:
                return
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self._arr[i][j] = newVal


r = Rect([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
print(r.getValue(0,2))
r.updateSubRectangle(0,0,3,2,5)
print(r._arr)
print(r.getValue(0,2))