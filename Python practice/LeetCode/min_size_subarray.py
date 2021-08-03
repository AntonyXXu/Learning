# https://leetcode.com/problems/minimum-size-subarray-sum/

def minSubArrLen(target, nums):
    if not nums:
        return 0
    left = 0
    right = 0
    curr = nums[right]
    length = None
    while right < len(nums):
        if curr < target:

            if right == len(nums) - 1:
                break
            right += 1
            curr += nums[right]
        elif curr >= target:
            if not length:
                length = right - left + 1
            if length == 1:
                return length
            else:
                length = min(length, right - left + 1)
            curr -= nums[left]
            left += 1

    if not length:
        return 0
    else:
        return length


print(minSubArrLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(minSubArrLen(target=4, nums=[1, 4, 4]))
print(minSubArrLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
print(minSubArrLen(11,    [1, 2, 3, 4, 5]))
