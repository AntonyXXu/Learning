# https://leetcode.com/problems/valid-sudoku/

def isValidSudoku(board):
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        rowSet = set()
        for col in range(cols):
            val = board[row][col]
            if val != ".":
                if val in rowSet:
                    return False
                rowSet.add(val)
    for col in range(cols):
        colSet = set()
        for row in range(rows):
            val = board[row][col]
            if val != ".":
                if val in colSet:
                    return False
                colSet.add(val)
    row = 0
    col = 0
    for row in range(0, rows, 3):
        for col in range(0, cols, 3):
            squareSet = set()
            r = row
            c = col
            for i in range(row, r + 3):
                for j in range(c, c + 3):
                    val = board[i][j]
                    if val != ".":
                        if val in squareSet:
                            return False
                        squareSet.add(val)
    return True

print(isValidSudoku( board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))