def fact(n):
    ans = 0
    while n > 0:
        n //= 5
        ans += n 
    return ans

print(fact(3))
print(fact(10))
print(fact(100))