# https://leetcode.com/problems/permutations-ii/

def permuteUnique(nums):
    if not nums:
        return nums
    ans = []
    prefix = []
    s = set()
    dfs(nums, prefix, ans, s)
    return ans

def dfs(nums, prefix, ans, s):
    if not nums:
        ans.append(prefix)
        s.add(tuple(prefix))
        return
    if tuple(prefix) in s:
        return 
    s.add(tuple(prefix))
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i+1:], prefix + [nums[i]], ans, s)

print(permuteUnique([1,1,2]))
print(permuteUnique([1,3,2]))

print(permuteUnique([]))
print(permuteUnique([1]))
