# https://leetcode.com/problems/split-array-largest-sum/

def splitArray(nums, m):
    def conditional(mid):
        counter = 1
        total = 0
        for num in nums:
            total += num
            if total > mid:
                total = num
                counter += 1
                if counter > m:
                    return False
        return True


    if not nums or not m:
        return 0
    left = max(nums)
    right = sum(nums)
    if m == 1:
        return right
    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1
    return left