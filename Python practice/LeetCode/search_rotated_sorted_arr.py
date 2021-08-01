# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    if not nums:
        return -1
    # Find pivot
    pivot = findPivot(nums)
    highIndex = pivot - 1
    if highIndex == -1:
        highIndex = len(nums) - 1
    if target < nums[pivot] or target > nums[highIndex]:
        return -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        mid = nums[m]
        if mid == target:
            return m
        elif mid < target and target <= nums[r]:
            l = m + 1
        elif mid > target and target >= nums[l]:
            r = m - 1
        elif mid < target and target >= nums[pivot]:
            r = highIndex
        elif mid > target and target <= nums[highIndex]:
            l = pivot

    return -1


def findPivot(nums):
    if len(nums) == 1:
        return 0
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        mid = nums[m]
        if mid > nums[m+1]:
            return m + 1
        if mid < nums[l]:
            l = m + 1
        else:
            r = m - 1
    return 0


print(findPivot(nums=[4, 5, 6, 7, 0, 1, 2]))
print(findPivot(nums=[4, 5, 6, 7, 0, 1, 2]))
print(findPivot(nums=[1]))
print(findPivot(nums=[1, 2, 3, 4]))

print(search([4, 5, 6, 7, 0, 1, 2], 0))
print(search([4, 5, 6, 7, 0, 1, 2], 3))
print(search([1], 0))
