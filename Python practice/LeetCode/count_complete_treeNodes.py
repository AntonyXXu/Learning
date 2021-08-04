# https://leetcode.com/problems/count-complete-tree-nodes/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: TreeNode) -> int:
    if not root:
        return 0
    left = count(root.left)
    right = count(root.right)
    if left == right:
        return countNodes(root.right) + 2 ** left
    else:
        return countNodes(root.left) + 2 ** right


def count(node):
    if not node:
        return 0
    return 1 + count(node.left)
