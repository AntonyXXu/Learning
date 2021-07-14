# https://leetcode.com/problems/4sum-ii/

import collections

def fourSumCount(nums1, nums2, nums3, nums4):
    ans = 0
    d = collections.Counter()
    for A in nums1:
        for B in nums2:
            total = A + B
            d[total] += 1
    for C in nums3:
        for D in nums4:
            total = -(C + D)
            if total in d:
                ans += d[total]
    return ans
print(fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]  ))
print(fourSumCount( nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]  ))
