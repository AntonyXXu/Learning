# https://leetcode.com/problems/binary-tree-pruning/

class Node:
    def __init__(self, val, left = None, right =None):
        self.val = val
        self.left = left
        self.right = right

def prune(root):
    if not root:
        return None
    root.left = prune(root.left)
    root.right = prune(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    else:
        return root