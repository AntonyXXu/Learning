# https://leetcode.com/problems/koko-eating-bananas/

def minEatingSpeed(piles, h):
    
    def conditional(threshold):
        hour = 0
        for pile in piles:
            hour += pile // threshold
            if pile % threshold != 0:
                hour += 1
            if hour > h:
                return False
        return True


    left = 1
    right = max(piles)

    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(minEatingSpeed([2,2], 2))