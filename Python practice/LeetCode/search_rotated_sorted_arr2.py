# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

def search(nums, target):
    l = 0
    r = len(nums) - 2
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True 
        if nums[mid] < nums[r]:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        elif nums[mid] > nums[r]:
            if nums[mid] > target >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            r -= 1
    return nums[l] == target
