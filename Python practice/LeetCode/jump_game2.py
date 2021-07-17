# https://leetcode.com/problems/jump-game-ii/

def jump(nums):
    if len(nums) <= 1:
        return 0
    ans = 0
    end = len(nums) - 1
    while end > 0:
        for i in range(end):
            if nums[i] >= end - 1:
                end = i
                ans += 1
                break
    return ans

def jump(nums):
    ans = 0
    prev = 0
    current = 0
    longest = nums[0]
    while prev < len(nums) - 1:
        longest = max(longest, current + nums[current])
        if current == prev:
            prev = longest
            ans += 1
        current += 1
    return ans

print(jump( [2,3,1,1,4] ))
print(jump(  [2,3,0,1,4] ))