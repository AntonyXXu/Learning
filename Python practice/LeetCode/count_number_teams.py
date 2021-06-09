# https://leetcode.com/problems/count-number-of-teams/
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
    
