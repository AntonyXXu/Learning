# https://leetcode.com/problems/single-number/

def singleNumber(nums):
    ans = 0
    for i in range(len(nums)):
        ans = ans ^ nums[i]
        print(ans)
    return ans

# print(singleNumber([2,2,1]))
# print(singleNumber([1]))
print(singleNumber([4,1,2,1,2]))