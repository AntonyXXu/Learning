# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

p1 =  [2,4,1,2,7,8]
p2 = [2,4,5]
p3 =  [9,8,7,6,5,1,2,3,4]

def getCoins(pile):
    p = sorted(pile)
    n = len(p) // 3
    res = 0
    i = len(p) - 2
    while n > 0:
        res += p[i]
        n -= 1
        i -= 2
    return res

print(getCoins(p1))
print(getCoins(p2))
print(getCoins(p3))