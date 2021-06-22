def s(nums, target):
    hi = len(nums)
    lo = 0
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return max(0, min(lo, len(nums)))


print(s(nums = [1,3,5,6], target = 5))
print(s(nums = [1,3,5,6], target = 2))
print(s(nums = [1,3,5,6], target = 7))
print(s(nums = [1,3,5,6], target = 0))
print(s(nums = [1], target = 0))