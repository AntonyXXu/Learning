# https://leetcode.com/problems/climbing-stairs/

def climbStairs(n):
    if n < 0:
        return 0
    if n <= 2:
        return n
    prev1 = 2
    prev2 = 1
    ans = 0

    for _ in range(2, n):
        ans = prev1 + prev2
        prev2 = prev1
        prev1 = ans

    return ans

print(climbStairs(2))
print(climbStairs(3))
print(climbStairs(4))
