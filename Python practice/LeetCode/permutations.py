# https://leetcode.com/problems/permutations/

def permutations(nums):
    ans = []
    prefix = []
    dfs(nums, ans, prefix)
    return ans

def dfs(nums, ans, prefix):
    if not nums:
        ans.append(prefix)
        return
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i+1:], ans, prefix + [nums[i]])

print(permutations([1,2,3]))
print(permutations([1,2]))