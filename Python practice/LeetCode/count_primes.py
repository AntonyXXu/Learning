def countPrimes(n):
    if n <= 2:
        return 0
    primes = [1] * n
    for i in range(2, int(n**0.5 + 1), 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = 0
    return sum(primes)

print(countPrimes(10))
print(countPrimes(10))
print(countPrimes(10))