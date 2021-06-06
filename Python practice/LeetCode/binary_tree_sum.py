# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumBT(root):
    return helper(root, 0)

def helper(node, val):
    if not node:
        return 0
    val = val * 2 + node.val
    if not node.left and not node.right:
        return val
    return helper(node.left,val) + helper(node.right,val)

    
