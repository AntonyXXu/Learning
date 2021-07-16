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

print(subsetsUnique(    [1,2,2] ))
print(subsetsUnique(    [1,2,3]))
print(subsetsUnique(    [1]))
        