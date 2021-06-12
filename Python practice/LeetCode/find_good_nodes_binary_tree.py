# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    max = root.val
    left = helper(root.left, max)
    right = helper(root.right, max)
    return left + right + 1

def helper(node, max):
    if not node:
        return 0
    res = 0
    if node.val >= max:
        max = node.val
        res = 1
    left = helper(node.left, max)
    right = helper(node.right, max)
    return res + left + right