def pwr(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 4 != 0:
        return False
    return pwr(n/4)

print(pwr(5))
print(pwr(16))
print(pwr(1))
print(pwr(0))