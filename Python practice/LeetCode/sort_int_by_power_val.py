# https://leetcode.com/problems/sort-integers-by-the-power-value/

l1 = 12
h1 = 15
k1 = 2

l2 = 1
h2 = 1
k2 = 1

l3 = 7
h3 = 11
k3 = 4

l4 = 5
h4 = 20
k4 = 10

l5 = 1
h5 = 1000
k5 = 777

def kth(lo, hi, k):
    nums = {}
    for i in range(lo, hi+1):
        counter = 0
        val = i
        while val != 1:
            if val%2 == 0:
                val //= 2
            else:
                val = val * 3 + 1
            counter += 1
        nums[i] = counter
    resArr = sorted(nums.keys(), key=nums.get)
    return resArr[k-1]

print(kth(l1,h1,k1))
print(kth(l2,h2,k2))
print(kth(l3,h3,k3))
print(kth(l4,h4,k4))
print(kth(l5,h5,k5))