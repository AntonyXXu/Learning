# https://leetcode.com/problems/battleships-in-a-board/
b1 = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
b2 = [["."]]
def countShips(b):
    count = 0
    for row in range(len(b)):
        for col in range(len(b[0])):
            if b[row][col] == 'X':
                if row == 0 and col == 0:
                    count += 1
                elif row == 0 and b[row][col-1] !='X':
                    count += 1
                elif col == 0 and b[row-1][col] != 'X':
                    count += 1
                elif b[row-1][col] != 'X' and b[row][col-1] != 'X':
                    count += 1
    return count

print(countShips(b1))
print(countShips(b2))