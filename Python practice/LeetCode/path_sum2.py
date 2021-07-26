# https://leetcode.com/problems/path-sum-ii/
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, targetSum):
    ans = []
    if not root:
        return ans
    prefix = []
    dfs(root, targetSum, prefix, ans)
    return ans
        
def dfs(node, targetSum, prefix, ans):
    if not node:
        return
    if not node.left and not node.right:
        if targetSum == node.val:
            ans.append(prefix + [node.val])
        return
    if node.left:
        dfs(node.left, targetSum - node.val, prefix + [node.val], ans)
    if node.right:
         dfs(node.right, targetSum - node.val, prefix + [node.val], ans)


t = TreeNode(1, TreeNode(2), TreeNode(3))

print(pathSum(t, 3))
print(pathSum(None ,0))