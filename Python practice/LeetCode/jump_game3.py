# https://leetcode.com/problems/jump-game-iii/

def canReach(arr, start):
    visited = [False] * len(arr)
    target = 0
    return dfs(arr, start, visited, target)

def dfs(arr, start, visited, target):
    if start < 0 or start >= len(arr) or visited[start]:
        return False
    if arr[start] == target:
        return True
    visited[start] = True
    return dfs(arr, start - arr[start], visited, target) \
        or dfs(arr, start + arr[start], visited, target)
print(canReach(   arr = [4,2,3,0,3,1,2], start = 5  ))
print(canReach(   arr = [4,2,3,0,3,1,2], start = 0   ))
print(canReach(  arr = [3,0,2,1,2], start = 2   ))
