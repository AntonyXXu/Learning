# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

def minDiff(nums):
    if len(nums) < 4:
        return 0

    nums.sort()

    ans1 = nums[-1] - nums[3]
    ans2 = nums[-2] - nums[2]
    ans3 = nums[-3] - nums[1]
    ans4 = nums[-4] - nums[0]

    return min(ans1, ans2, ans3, ans4)
