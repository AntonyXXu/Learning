# https://leetcode.com/problems/next-permutation/

def nextPermutation(nums):
    i = len(nums) - 1
    j = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:
        nums.reverse()
        return 
    pivot = i - 1
    while nums[j] <= nums[pivot]:
        j -= 1
    nums[j], nums[pivot] = nums[pivot], nums[j]
    left = pivot + 1
    right = len(nums) -1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    
    return nums

print(nextPermutation([1,2,3]))
print(nextPermutation([3,2,1]))
print(nextPermutation([1,1,3]))
print(nextPermutation([1,3,1]))