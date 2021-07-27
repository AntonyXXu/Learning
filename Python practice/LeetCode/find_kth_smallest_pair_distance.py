# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

def smallestDistancePair(self, nums, k: int) -> int:
    def condition(mid):
        leftptr = 0
        rightptr = 0
        counter = 0
        while leftptr < len(nums) or rightptr < len(nums):
            while rightptr < len(nums) and nums[rightptr] - mid <= nums[leftptr]:
                rightptr += 1
            counter += rightptr - leftptr - 1
            leftptr += 1
        return counter >= k

    nums.sort()
    left = 0
    right = nums[-1] - nums[0]
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left

