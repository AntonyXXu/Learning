# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

def minDays(bloomDay, m, k):
    if len(bloomDay) < m * k:
        return -1
    
    def conditional(mid):
        bouquets = 0
        flowers = 0
        for flower in bloomDay:
            if flower > mid:
                flowers = 0
            else:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
                if bouquets >= m:
                    return True
        return False

    left = 1
    right = max(bloomDay)
    while left < right:
        mid = left + (right - left) // 2
        if conditional(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))