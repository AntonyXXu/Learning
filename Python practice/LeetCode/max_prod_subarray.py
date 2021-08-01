# https: // leetcode.com/problems/maximum-product-subarray/

def maxProd(nums):
    if not nums:
        return nums
    if len(nums) == 1:
        return nums[0]
    left = nums[0]
    right = nums[-1]
    leftM = nums[0]
    rightM = nums[-1]
    for i in range(1, len(nums)):
        if left == 0:
            left = nums[i]
        else:
            left *= nums[i]
        if right == 0:
            right = nums[-1-i]
        else:
            right *= nums[-1-i]
        leftM = max(left, leftM)
        rightM = max(right, rightM)
    return max(leftM, rightM)


# print(maxProd(nums=[-2, 0, -1]))
print(maxProd([-1, -2, -3, 0]))
