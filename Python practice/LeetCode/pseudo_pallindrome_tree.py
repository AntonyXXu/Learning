# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pseudoPalindromicPaths(root):
    d = collections.Counter()
    return helper(root, d)

def helper(node: TreeNode, d: collections.Counter):
    if not node:
        return 0
    d[node.val] += 1    
    # check the left side
    left = helper(node.left, d)
    # check the right side
    right = helper(node.right, d)
    res = left + right
    if not node.left and not node.right:
        res = checkPallindrome(d)
    d[node.val] -= 1
    return res

def checkPallindrome(d: collections.Counter):
    odd = 0
    for counter in d:
        if d[counter] % 2 == 1:
            odd += 1
        if odd > 1:
            return 0
    return 1

r = TreeNode(2)
r.left = TreeNode(3)
r.right = TreeNode(1)
r.left.left = TreeNode(3)
r.left.right = TreeNode(1)
r.right.right = TreeNode(1)

