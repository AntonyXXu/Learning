# https://leetcode.com/problems/house-robber-ii/


def prevRob(nums, left, right):
    if not nums:
        return 0
    if right - left <= 1:
        return max(nums[left], nums[right])
    prev2 = 0
    prev1 = 0
    for i in range(left, right):
        curr = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = curr
    return curr


def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    return max(prevRob(nums, 0, len(nums) - 1), prevRob(nums, 1, len(nums)))
