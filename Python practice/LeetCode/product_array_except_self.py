# https://leetcode.com/problems/product-of-array-except-self/

def prod(nums):
    if not nums:
        return nums

    leftTrav = [1]*len(nums)
    rightTrav = [1]*len(nums)
    for i in range(len(nums)):
        if i == 0:
            leftTrav[i] = 1
            rightTrav[len(nums)-1 - i] = 1
        else:
            leftTrav[i] = leftTrav[i-1] * nums[i-1]
            rightTrav[len(nums) - 1 - i] = rightTrav[len(nums) -
                                                     i] * nums[len(nums) - i]

    for i in range(len(nums)):
        leftTrav[i] *= rightTrav[i]

    return leftTrav


print(prod(nums=[1, 2, 3, 4]))
print(prod([-1, 1, 0, -3, 3]))
