def attack(queens, king):
    rows = 8
    cols = 8
    r = king[0]
    c = king[1]
    ans = []
    while r >= 0:
        if [r, c] in queens:
            ans.append([r,c])
            break
        r -= 1
    r = king[0]
    c = king[1]
    while r < rows:
        if [r,c] in queens:
            ans.append([r,c])  
            break
        r += 1
    r = king[0]
    c = king[1]
    while c >= 0:
        if [r, c] in queens:
            ans.append([r,c])
            break
        c -= 1
    r = king[0]
    c = king[1]
    while c < cols:
        if [r,c] in queens:
            ans.append([r,c])  
            break
        c += 1
    r = king[0]
    c = king[1]
    while r >= 0 and c >= 0:
        if [r, c] in queens:
            ans.append([r,c])
            break
        r -= 1
        c -= 1
    r = king[0]
    c = king[1]
    while r < rows and c < cols:
        if [r, c] in queens:
            ans.append([r,c])
            break
        r += 1
        c += 1
    r = king[0]
    c = king[1]
    while r >= 0 and c < cols:
        if [r, c] in queens:
            ans.append([r,c])
            break
        r -= 1
        c += 1
    r = king[0]
    c = king[1]
    while r < rows and c >= 0:
        if [r, c] in queens:
            ans.append([r,c])
            break
        r += 1
        c -= 1
    return ans
    
print(attack(queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]))
print(attack(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
print(attack(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))
