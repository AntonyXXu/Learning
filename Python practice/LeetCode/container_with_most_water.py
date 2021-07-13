# https://leetcode.com/problems/container-with-most-water/
def maxArea(height):
    left = 0
    right = len(height) - 1
    ans = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        ans = max(area, ans)
        if height[left] < height[right]:   
            left += 1
        else:
            right -= 1
    return ans

print(maxArea( [1,8,6,2,5,4,8,3,7]))
print(maxArea( [1,1]))
print(maxArea([4,3,2,1,4]))
print(maxArea( [1,2,1]))
