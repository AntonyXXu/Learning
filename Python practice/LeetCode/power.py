# https://leetcode.com/problems/powx-n/

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 1:
        return power(x, n-1) * x
    else:
        return power (x * x, n // 2)
