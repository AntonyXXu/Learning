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

    


print(sortColors( [2,0,2,1,1,0]))
print(sortColors( [2,0,1]))
print(sortColors( [0]))