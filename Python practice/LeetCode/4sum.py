# https://leetcode.com/problems/4sum/

def fourSum(nums, target):
    l = 0
    r = len(nums) - 1
    ans = set()
    nums.sort()
    prefix = []
    N = 4
    nSum(l, r, N, target, nums, ans, prefix)
    res = []
    for obj in ans:
        temp = []
        for num in obj:
            temp.append(num)
        res.append(temp)
    return res
    
def nSum(l, r, N, target, nums, ans, prefix):
    if len(nums) < N:
        return
    if N == 2:
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                oneRes = prefix + [nums[l], nums[r]]
                ans.add(tuple(oneRes))
                l += 1
                r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(l, r - N + 2):
            if i == l or (i > l and nums[i] != nums[i-1]):
                nSum(i + 1, r, N-1, target - nums[i], nums, ans, prefix + [nums[i]])
    
print(fourSum( nums = [1,0,-1,0,-2,2], target = 0))
print(fourSum( nums = [2,2,2,2,2], target = 8))
print(fourSum( nums = [0,0,0,0], target = 0))
print(fourSum([-2,-1,-1,1,1,2,2], 0))
