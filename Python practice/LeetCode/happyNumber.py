def happyNumber(n):
    history = set()
    while True:
        curr = ""
        while n > 0:
            curr += str((n%10))
            n //= 10
        if curr in history:
            return False
        for num in curr:
            n += int(num) ** 2
        if n == 1:
            return True
        history.add(curr)

print(happyNumber(1))
print(happyNumber(5))
print(happyNumber(19))
print(happyNumber(2))