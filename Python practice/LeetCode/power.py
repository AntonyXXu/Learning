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

def power(x, n):
    if n == 0:
        return 1
    negative = False
    if n < 0:
        negative = True
        n *= -1
    ans = 1
    while n > 0:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            ans *= x
            n -= 1

    if negative:
        ans = 1 / ans
    return ans


