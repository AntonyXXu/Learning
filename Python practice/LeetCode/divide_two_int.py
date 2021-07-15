# https://leetcode.com/problems/divide-two-integers/

def divide(dividend, divisor):
    if (dividend == -2147483648 and divisor == -1): return 2147483647
    positive = (dividend > 0) == (divisor>0)
    i = 32
    while i:

        i-= 1

print(divide(10, 3 ))
print(divide(7, -3 ))
print(divide(0, 1 ))
print(divide(1, 1 ))
print(divide(-1, 1 ))
print(divide(-2147483648,-1))