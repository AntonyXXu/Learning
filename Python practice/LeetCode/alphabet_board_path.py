# https://leetcode.com/problems/alphabet-board-path/
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = []
        row = 0
        col = 0
        for letter in target:
            target_row, target_col = findCoords(letter)
            if col > 0:
                if col <= target_col:
                    for i in range(col, target_col):
                        ans.append('R')
                elif col > target_col:
                    for i in range(col, target_col , -1):
                        ans.append('L')
                if row <= target_row:
                    for i in range(row, target_row):
                        ans.append('D')
                elif row > target_row:
                    for i in range(row, target_row , -1):
                        ans.append('U')
            else:
                if row <= target_row:
                    for i in range(row, target_row):
                        ans.append('D')
                elif row > target_row:
                    for i in range(row, target_row , -1):
                        ans.append('U')
                if col <= target_col:
                    for i in range(col, target_col):
                        ans.append('R')
                elif col > target_col:
                    for i in range(col, target_col , -1):
                        ans.append('L')
            row = target_row
            col = target_col
            ans.append('!')
        return ''.join(ans)

def findCoords(letter):
    cols = 5
    row = (ord(letter) - ord('a')) // cols
    col = (ord(letter) - ord('a')) % cols
    return (row, col)
