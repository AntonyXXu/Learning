# https://leetcode.com/problems/combination-sum-iii/

def combinationSum3(k, n):
    nums = [i + 1 for i in range(9)]
    index = 0
    ans = []
    prefix = []
    dfs(nums, n, k, index, prefix, ans)
    return ans

def dfs(nums, n, k, index, prefix, ans):
    if n == 0 and k == 0:
        ans.append(prefix)
    if n <= 0 or k <= 0:
        return 
    
    for i in range(index, len(nums)):
        dfs(nums, n - nums[i], k-1, i + 1, prefix + [nums[i]], ans)

print(combinationSum3(3, 7))
print(combinationSum3(3, 9))
print(combinationSum3(4, 1))
print(combinationSum3(3, 2))
print(combinationSum3(9, 45))
print(combinationSum3(2, 18))