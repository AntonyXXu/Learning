
r = 1
c = 4
rs = 0
cs = 0

rows = 5
cols = 6
rStart = 1
cStart = 4

def spiral(rows, cols, rStart, cStart):
    res = []
    r = rStart
    c = cStart
    inc = 1
    while len(res) < rows * cols:
        res.append([r,c])
        for i in range(inc):
            r += inc
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        for j in range(inc):
            c += inc
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        inc += 1
        for i in range(inc):
            r -= inc
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        for j in range(inc):
            r -= inc
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        inc += 1
    return res

print(spiral(r,c,rs,cs))
print(spiral(rows,cols,rStart,cStart))
