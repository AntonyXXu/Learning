# https://leetcode.com/problems/zigzag-conversion/

def zigzag(s, rows):
    res = [''] * rows
    row = 0
    step = -1
    if rows == 1:
        step = 0
    for i in range(len(s)):
        res[row] += s[i]
        if row == 0 or row == rows-1:
            step = -step
        row += step
    return ''.join(res)

print(zigzag('PAYPALISHIRING', 3))
print(zigzag('PAYPALISHIRING', 4))
print(zigzag('aB',1))