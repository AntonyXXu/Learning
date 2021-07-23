# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
from math import ceil
def smallestDivisor(nums, threshold):
    left = 0
    right = max(nums)
    while left < right:
        mid = (left + right) // 2
        if mid == 0:
            return 1
        calcThresh = total(nums, mid)
        if calcThresh <= threshold:
            right = mid
        elif calcThresh > threshold:
            left = mid + 1
    return right

def total(nums, div):
    ret = 0
    for num in nums:
        ret += ceil(num/div)
    return ret

print(smallestDivisor(  nums = [1,2,5,9], threshold = 6    ))
print(smallestDivisor(    nums = [44,22,33,11,1], threshold = 5  ))
print(smallestDivisor(   nums = [21212,10101,12121], threshold = 1000000   ))
print(smallestDivisor(    nums = [2,3,5,7,11], threshold = 11   ))
print(smallestDivisor([909771,973275,979226,934386,981517], 10))