# https://leetcode.com/problems/subsets-ii/

def subsetsUnique(nums):
    ans = [[]]
    nums.sort()
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            l = len(ans)
        for j in range(len(ans) - l, len(ans)):
            ans.append(ans[j] + [nums[i]])
    return ans

def subsetsUnique(nums):
    ans = []
    nums.sort()
    prefix = []
    index = 0
    dfs(nums, index, prefix, ans)
    return ans

def dfs(nums, index, prefix, ans):
    ans.append(prefix)
    if index >= len(nums):
        return
    for i in range(index, len(nums)):
        if i > 0 and i <= index:
            print(i ,  index)
        if i > index and nums[i] == nums[i-1]:
            continue
        dfs(nums, i + 1, prefix + [nums[i]], ans)
        
print(subsetsUnique(    [1,2,2] ))
print(subsetsUnique(    [1,2,3]))
print(subsetsUnique(    [1]))
        