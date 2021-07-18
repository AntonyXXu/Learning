# https://leetcode.com/problems/sort-colors/

def sortColors(nums):
    if not nums:
        return nums
    #Only 1, 2, 3
    d = {0: 0, 1: 0, 2: 0}
    for num in nums:
        d[num] += 1
    curr = 0
    for i in range(len(nums)):
        while d[curr] == 0:
            curr += 1
            if curr > 2:
                break
        nums[i] = curr
        d[curr] -= 1

def sortColors(nums):
    p1 = 0
    p2 = 0
    p3 = len(nums) - 1
    while p2 <= p3:
        if nums[p2] == 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
        elif nums[p2] == 1:
            p2 += 1
        else:
            nums[p2], nums[p3] = nums[p3], nums[p2]
            p3 -= 1
    print(nums)

print(sortColors( [2,0,2,1,1,0]))
print(sortColors( [2,0,1]))
print(sortColors( [0]))