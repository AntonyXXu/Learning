
nums = [1,12,-5,-6,50,3]
k = 4

def calc(nums, k):
    total = sum(nums[:k])
    maximum = total
    for i in range(k, len(nums)):
        total += nums[i]
        total -= nums[i-k]
        maximum = max(total, maximum)
    return maximum / k

print(calc(nums, k))
print(calc([5],1))
