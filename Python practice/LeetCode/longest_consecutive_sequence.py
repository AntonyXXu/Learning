# https://leetcode.com/problems/longest-consecutive-sequence/

def longest(nums):
    if not nums:
        return 0
    s = set(nums)
    ans = 0
    for num in nums:
        if num-1 not in s:
            curr = 1
            nextV = num + 1
            while nextV in s:
                curr += 1
                nextV += 1   
            ans = max(curr, ans)
    return ans
        
print(longest(   [100,4,200,1,3,2]))
print(longest(  [0,3,7,2,5,8,4,6,0,1]))