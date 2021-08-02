# https://leetcode.com/problems/house-robber/

def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    prev1 = 0
    prev2 = 0

    for i in range(len(nums)):
        temp = max(prev2 + nums[i], prev1)

        prev2 = prev1
        prev1 = temp
    return prev1


print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))
print(rob([2, 1, 1, 2]))
