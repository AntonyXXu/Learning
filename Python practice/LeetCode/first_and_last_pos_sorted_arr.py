# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchRange(nums, target):
    l = 0
    r = len(nums) - 1
    ans = [-1, -1]
    found = False
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            found = m
            break
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    
    if found is not False:
        l = m
        r = m
        while nums[l] == target and l >= 0:
            ans[0] = l
            l -= 1
        while r < len(nums) and nums[r] == target:
            ans[1] = r
            r += 1
    return ans

print(searchRange(nums = [5,7,7,8,8,10], target = 8))
print(searchRange( nums = [5,7,7,8,8,10], target = 6))
print(searchRange(nums =[], target = 8))
print(searchRange(nums =[8], target = 8))