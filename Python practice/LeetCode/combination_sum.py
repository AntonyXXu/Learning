# https://leetcode.com/problems/combination-sum/

def combinationSum(candidates, target): 
    index = 0
    ans = []
    prefix = []
    helper(candidates, target, ans, prefix, index)
    return ans
    

def helper(candidates, target, ans, prefix, index):
    if target == 0:
        ans.append(prefix)
    elif target < 0 or index >= len(candidates):
        return 
    for i in range(index, len(candidates)):
        helper(candidates, target - candidates[i], ans, prefix + [candidates[i]], i)
    


print(combinationSum( candidates = [2,3,5], target = 8))
print(combinationSum( candidates = [2], target = 1 ))
print(combinationSum(candidates = [1], target = 1 ))
print(combinationSum( candidates = [1], target = 2))