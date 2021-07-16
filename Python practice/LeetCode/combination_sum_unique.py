# https://leetcode.com/problems/combination-sum-ii/

def combinationSumUnique(nums, target):
    ans = []
    nums.sort()
    prefix = []
    index = 0
    dfs(nums, target, index, prefix, ans)
    return ans

def dfs(nums, target, index, prefix, ans):
    if target == 0:
        ans.append(prefix)
        return
    if target < 0:
        return 
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue
        if nums[i] > target:
            return
        dfs(nums, target - nums[i], i + 1, prefix + [nums[i]], ans)
    
print(combinationSumUnique( nums = [10,1,2,7,6,1,5], target = 8 ))
print(combinationSumUnique( nums = [2,5,2,1,2], target = 5 ))