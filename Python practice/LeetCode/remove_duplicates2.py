# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    ptr = 2
    for i in range(2, len(nums)):
        if nums[ptr-2] != nums[i]:
            nums[ptr] = nums[i]
            ptr += 1
    return ptr