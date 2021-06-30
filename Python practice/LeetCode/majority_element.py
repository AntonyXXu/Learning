def majority(nums):
    n = {}
    for num in nums:
        if num not in n:
            n[num] = 0
        else:
            n[num] += 1
    return max(n)

print(majority([2,2,1,1,1,2,2]))
print(majority([3,2,3]))

def m(nums):
    nums.sort()
    return nums[(len(nums))//2]


print(m([2,2,1,1,1,2,2]))
print(m([3,2,3]))