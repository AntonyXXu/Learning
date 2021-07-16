# https://leetcode.com/problems/subsets/

# def subsets(nums):
#     ans = []
#     prefix = []
#     dfs(nums, prefix, ans)
#     return ans

# def dfs(nums, prefix, ans, s):
#     if prefix:
#         prefix.sort()
#     if tuple(prefix) not in s:
#         s.add(tuple(prefix))
#         ans.append(prefix)
#     if not nums:
#         return
#     for i in range(len(nums)):
#         dfs(nums[:i] + nums[i+1:], prefix + [nums[i]], ans, s)

# Way too slow...

def subsets(nums):
    ans = []
    prefix = []
    index = 0
    dfs(nums, index, prefix, ans)
    return ans

def dfs(nums, index, prefix, ans):
    ans.append(prefix)
    if not nums:
        return
    for i in range(index, len(nums)):
        dfs(nums, i + 1,  prefix + [nums[i]], ans)

def subsets(nums):
    ans = [[]]
    for prefix in nums:
        ans.extend([i + [prefix] for i in ans] )
    return ans

def subsets(nums):
    ans = [[]]
    for num in nums:
        temp = []
        for prefix in ans:
            temp.append(prefix + [num])
        ans.extend(temp)
    return ans

print(subsets( [1,2,3] ))
print(subsets( [] ))
