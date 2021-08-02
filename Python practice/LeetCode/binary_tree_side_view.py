# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightView(root):
    if not root:
        return []
    ans = []
    h = set()
    height = 0
    preorder(root, ans, h, height)
    return ans


def preorder(root, ans, h, height):
    if not root:
        return
    if height not in h:
        h.add(height)
        ans.append(root.val)
    preorder(root.right, ans, h, height + 1)
    preorder(root.left, ans, h, height + 1)
