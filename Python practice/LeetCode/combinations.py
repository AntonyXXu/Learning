# https://leetcode.com/problems/combinations/

def combinations(n, k):
    if k > n:
        return []
    ans = []
    index = 1
    prefix = []
    dfs(n, k, index, prefix, ans)
    return ans

def dfs(n, k, index, prefix, ans):
    if k == 0:
        ans.append(prefix)
        return
    if k > n:
        return 
    for i in range(index, n+ 1):
        dfs(n, k - 1, i + 1, prefix + [i], ans)

print(combinations(4, 2))
print(combinations(1, 1))
