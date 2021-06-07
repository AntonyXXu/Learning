# https://leetcode.com/problems/score-after-flipping-matrix/

def score(m):
    if not m:
        return 0
    rows = len(m)
    cols = len(m[0])
    for row in range(rows):
        if m[row][0] == 0:
            for col in range(cols):
                m[row][col] = 1 - m[row][col] # convert to 1 or 0
        
    for col in range(cols):
        ctr_1 = 0
        ctr_0 = 0
        for row in range(rows):
            if m[row][col] == 0:
                ctr_0 += 1
            else:
                ctr_1 += 1
        if ctr_0 > ctr_1:
            for row in range(rows):
                m[row][col] = 1 - m[row][col]
    total = 0
    for row in range(rows):
        rowTotal = 0
        for col in range(cols):
            rowTotal = m[row][col] + rowTotal * 2
        total += rowTotal
    return total