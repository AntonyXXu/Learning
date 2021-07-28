# https://leetcode.com/problems/sum-root-to-leaf-numbers/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def sumNumbers(self, root):
        if not root:
            return 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, node, currVal):
        if not node.left and not node.right:
            self.ans += currVal + node.val
        currVal = currVal + node.val
        if node.left:
            self.dfs(node.left, currVal * 10)
        if node.right:
            self.dfs(node.right, currVal * 10)

n = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().sumNumbers(n))