# https://leetcode.com/problems/arithmetic-subarrays/

nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
nums1 = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l1 = [0,1,6,4,8,7]
r1 = [4,4,9,7,9,10]


def arith(nums, l, r):
    if not nums or not l or not r:
        return []
    res = [False for i in range(len(l))]
    for i in range(len(l)):
        left = l[i]
        right = r[i]
        if left == right:
            res[i] = True
        else: 
            splice = nums[left:right + 1]
            splice.sort()
            diff = splice[1] - splice[0]
            arithmetic = True
            for j in range(len(splice)-1):
                if splice[j+1] - splice[j] != diff:
                    arithmetic = False
            res[i] = arithmetic
    return res

print(arith(nums, l, r))
print(arith(nums1, l1, r1))
