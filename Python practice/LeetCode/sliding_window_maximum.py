# https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
def maxSlidingWindow(nums, k):
    dq = deque()
    ans = []
    for i in range(len(nums)):
        currVal = nums[i]
        while dq and currVal >= nums[dq[-1]]:
            dq.pop()
        while dq and dq[0] <= i - k:
            dq.popleft()
        dq.append(i)
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans

# print(maxSlidingWindow(     [1,3,-1,-3,5,3,6,7], k = 3     ))
# print(maxSlidingWindow(     [1], 1    ))
# print(maxSlidingWindow(    [1,-1], 1     ))
# print(maxSlidingWindow(  [9,11], 2       ))
print(maxSlidingWindow([7,2,4], 2))
        