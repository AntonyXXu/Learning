# https://leetcode.com/problems/fibonacci-number/

def fib(n):
    if n <= 1:
        return n
    prev1 = 1
    prev2 = 0
    ans = 0
    for _ in range(1, n):
        ans = prev1 + prev2
        prev2 = prev1
        prev1 = ans

    return ans

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
