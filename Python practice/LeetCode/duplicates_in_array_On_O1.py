def dup(nums):
    ans = []
    for i in range(len(nums)):
        while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
            val = nums[i] - 1
            nums[val], nums[i] = nums[i], nums[val]
    for i in range(len(nums)):
        if i != nums[i] - 1:
            ans.append(nums[i])
    return ans

print(dup([4,3,2,7,8,2,3,1]))
print(dup([1,1,2]))
print(dup([1]))