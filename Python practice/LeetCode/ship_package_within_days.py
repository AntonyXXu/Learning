# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

def shipWithinDays(weights, days):
    def conditional(mid):
        day = 1
        total = 0
        for weight in weights:
            total += weight
            if total > mid:
                day += 1
                total = weight
                if day > days:
                    return False
        return True

    left = max(weights)
    right = sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1
    return left