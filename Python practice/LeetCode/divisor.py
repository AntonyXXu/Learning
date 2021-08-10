def divisor(nums):
    def conditional(mid):
        for num in nums:
            if num % mid != 0:
                return False
        return True
    left = 1
    right = min(nums)
    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1

    return left
