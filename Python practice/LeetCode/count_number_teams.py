# https://leetcode.com/problems/count-number-of-teams/
from typing import List


t1 = [2,5,3,4,1]
t2 = [2,1,3]
t3 = [1,2,3,4]

def numTeams(t):
    res = 0
    for i in range(len(t)):
        for j in range(i, len(t)):
            for k in range(j,len(t)):
                if t[i] > t[j] and t[j] > t[k]:
                    res += 1
                if t[i] < t[j] and t[j] < t[k]:
                    res += 1
    return res

print(numTeams(t1))
print(numTeams(t2))
print(numTeams(t3))

def opt(t : List[int])-> int:
    res = 0
    for i in range(len(t)):
        leftLess = 0
        rightLess = 0
        leftMore = 0
        rightMore = 0
        for j in range(len(t)):
            if j < i:
                if t[j] < t[i]:
                    leftLess += 1
                else:
                    leftMore += 1
            elif j > i:
                if t[i] < t[j]:
                    rightMore += 1
                else:
                    rightLess += 1
        res += leftLess * rightMore + leftMore * rightLess
    return res

print(opt(t1))
print(opt(t2))
print(opt(t3))
