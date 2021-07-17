# https://leetcode.com/problems/jump-game/

def canJump(nums):
    jumps = nums[0]
    end = len(nums) - 1
    for i in range(len(nums)):
        jumps = max(nums[i], jumps)
        if i == end:
            return True
        if jumps == 0:
            return False
        jumps -= 1
    return True



print(canJump(nums = [2,3,1,1,4]))
print(canJump(nums = [3,2,1,0,4]))
print(canJump(nums = [0]))
print(canJump(nums = [2,0]))
    