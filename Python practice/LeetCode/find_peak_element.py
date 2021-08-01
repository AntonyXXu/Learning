# https://leetcode.com/problems/find-peak-element/

def findPeak(nums):
    def conditional(mid):
        return nums[mid] > nums[mid+1]

    if len(nums) == 1:
        return 0
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(findPeak([6, 5, 4, 3, 2, 3, 2]))
