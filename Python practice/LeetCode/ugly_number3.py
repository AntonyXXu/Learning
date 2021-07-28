# https://leetcode.com/problems/ugly-number-iii/
import math
def nthUgly(n, a, b, c):
    def condition(mid):
        ctr = 0
        ctr += mid // a + mid // b + mid // c
        ctr -= mid // ab + mid // ac + mid // bc
        ctr += mid // abc
        return ctr >= n

    ab = a*b// math.gcd(a, b)
    ac = a*c//math.gcd(a, c)
    bc = b*c//math.gcd(b, c)
    abc = a*bc//math.gcd(a, bc)

    left = min(a, b, c)
    right = n*abc
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left