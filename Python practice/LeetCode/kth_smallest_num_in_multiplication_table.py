# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/

def findKthNumber( m, n, k):
    def condition(mid):
        counter = 0
        for i in range(1, m + 1):
            addVal = min(mid // i, n)
            counter += addVal
            if counter >= k:
                return False
        return True

    left = 1
    right = m * n
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            left = mid + 1
        else:
            right = mid
    return left