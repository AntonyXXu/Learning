# You are given the logs for users' actions on LeetCode, and an integer k. 
# The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] 
# indicates that the user with IDi performed an action at the minute timei.

# Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

# The user active minutes (UAM) for a given user is defined as the number of unique minutes in which 
# the user performed an action on LeetCode. 
# A minute can only be counted once, even if multiple actions occur during it.

# You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.
# https://leetcode.com/problems/finding-the-users-active-minutes/

logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
logs1 = [[1,1],[2,2],[2,3]]
k1 = 4

def userActiveMins(logs, k):
    res = [0 for i in range(k)] 
    logset = set()
    for item in logs:
        logset.add((item[0], item[1]))
    userDict = {}         
    for item in logset:
        if item[0] not in userDict:
            userDict[item[0]] = 1
        else:
            userDict[item[0]] += 1
    for key, val in userDict.items():
        res[val-1] += 1

    return res

print(userActiveMins(logs, k))
print(userActiveMins(logs1, k1))