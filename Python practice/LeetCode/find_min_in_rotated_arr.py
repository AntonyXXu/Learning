# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    def conditional(mid, left, right):
        return nums[mid] <= nums[right]

    if not nums:
        return
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid, left, right):
            right = mid
        else:
            left = mid + 1
    return nums[left]
