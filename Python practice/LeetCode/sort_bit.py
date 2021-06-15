a1 =  [0,1,2,3,4,5,6,7,8]
a2 = [1024,512,256,128,64,32,16,8,4,2,1]
a3 =  [10000,10000]
a4 = [2,3,5,7,11,13,17,19]

def bits(n):
    ans = 0
    while n > 0:
        if n%2 == 1:
            ans += 1
        n //= 2
    return ans

def compareV(n):
    return (bits[n], n)

def sortbits(arr):
    return sorted(arr, key = lambda n: [bits(n), n])

print(sortbits(a1))
print(sortbits(a2))
print(sortbits(a3))
print(sortbits(a4))
