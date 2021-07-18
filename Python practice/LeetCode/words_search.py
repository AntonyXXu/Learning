# https://leetcode.com/problems/word-search/

class Solution:
    def __init__(self):
        self.found = False
    
    def exist(self, board, word):
        self.found = False
        word_i = 0        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, word_i, i, j):
                    return True
        return False

    def dfs(self, board, word, word_i, row, col):
        if self.found:
            return True
        
        if word_i == len(word) :
            self.found = True
            return True
       
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False
        
        currentChar = board[row][col]
        if currentChar != word[word_i]:
            return False

        board[row][col] = '#'

        returnVal = self.dfs( board, word, word_i + 1, row + 1, col) \
            or self.dfs( board, word, word_i + 1, row - 1, col) \
            or self.dfs( board, word, word_i + 1, row, col + 1)  \
            or self.dfs( board, word, word_i + 1, row, col - 1) 
        board[row][col] = currentChar

        return returnVal
        



c = Solution()

print(c.exist(       board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"    ))
print(c.exist(   board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"       ))
print(c.exist(     board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"     ))
    