# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

m1 = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

m2 = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

def result(m):
    rows = len(m)
    cols = len(m[0])
    res = 0
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == 1:
                if row and col:
                    m[row][col] = min(m[row-1][col],m[row-1][col-1],m[row][col-1]) + m[row][col]
                res+= m[row][col]
    return res

print(result(m1))
print(result(m2))