# https://leetcode.com/problems/construct-the-rectangle/

def constructRectangle(area):
    if area == 0:
        return [0,0]
    s = int(area**0.5) + 1
    while s > 0:
        if area % s == 0:
            return [max(area // s, s), min(area // s, s)]
        s -= 1

print(constructRectangle(37))
print(constructRectangle(122122))