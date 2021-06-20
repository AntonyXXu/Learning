
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
    res.append([r,c])
    while len(res) < rows * cols:
        for j in range(inc):
            c += 1
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        for i in range(inc):
            r += 1
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])

        inc += 1
        for i in range(inc):
            c -= 1
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        for j in range(inc):
            r -= 1
            if r < rows and c < cols and r >= 0 and c >= 0:
                res.append([r,c])
        inc += 1
    return res

print(spiral(r,c,rs,cs))
print(spiral(rows,cols,rStart,cStart) == [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])
