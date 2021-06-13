
def twoEggs(n):
    ans = 1
    while n - ans > 0:
        n -= ans
        ans += 1
        
    return ans

print(twoEggs(100))