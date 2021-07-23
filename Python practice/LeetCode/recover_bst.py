# https://leetcode.com/problems/recover-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recover(self, root):
        self.swap1 = None
        self.swap2 = None
        self.prev = None
        self.inorder(root)
        self.swap1.val, self.swap2.val = self.swap2.val, self.swap1.val

    def inorder(self, node):
        if not node:
            return 
        self.inorder(node.left)

        if not self.swap1 and (self.prev and self.prev.val >= node.val):
            self.swap1 = self.prev
        if self.swap1 and self.prev.val >= node.val:
            self.swap2 = node
        self.prev = node

        self.inorder(node.right)