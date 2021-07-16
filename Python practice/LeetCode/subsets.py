# https://leetcode.com/problems/subsets/

def subsets(nums):
    ans = []
    prefix = []
    s = set()
    dfs(nums, prefix, ans, s)
    return ans

def dfs(nums, prefix, ans, s):
    if prefix:
        prefix.sort()
    if tuple(prefix) not in s:
        s.add(tuple(prefix))
        ans.append(prefix)
    if not nums:
        return
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i+1:], prefix + [nums[i]], ans, s)

print(subsets( [1,2,3] ))
print(subsets( [] ))
