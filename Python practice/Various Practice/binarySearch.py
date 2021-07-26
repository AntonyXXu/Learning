# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/777019/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.

# Minimize k , s.t. condition(k) is True
def bsearch(nums, conditional):
    def condition(value) -> bool:
        pass

    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


