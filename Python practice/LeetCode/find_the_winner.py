# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
import collections

def findTheWinner(n, k):
    res = 0
    a = [i for i in range(1,n+1)]
    i = 0
    for j in range(n):
        i = (i+k-1)%n
        res = a.pop(i)
        n -= 1
    return res

print(findTheWinner(5,2))
print(findTheWinner(6,5))