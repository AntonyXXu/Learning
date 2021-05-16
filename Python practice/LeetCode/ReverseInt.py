x = 123
y = -123
z = 0
n = 120

def reverseInt(num):
    if num == 0:
        return 0
    negative = False
    if num < 0:
        negative = True
        num *= -1
    res = 0
    while num > 0:
        res = 10*res + num % 10
        num = num // 10
    return res if not negative else -res

print(reverseInt(x))
print(reverseInt(y))
print(reverseInt(z))
print(reverseInt(n))