# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    previous = None
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.previous
        root.left = None
        self.previous = root