def threeSumClosest(nums, target):
    if len(nums) < 3:
        raise Exception("Error, too few arguments")
    nums.sort()
    ans = nums[0] + nums[1] + nums[2] - target
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            diff = total - target
            if abs(diff) <= abs(ans):
                ans = diff
            if total == target:
                return total
            elif total < target:
                left += 1
            else:
                right -= 1
    return ans + target

            
print(threeSumClosest( [-1,2,1,-4], 1))
print(threeSumClosest( [0,2,1,-3], 1))
        