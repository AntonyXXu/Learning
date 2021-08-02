# https://leetcode.ca/all/156.html
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def upsideDown(root):
    if not root or not root.left:
        return root
    leftNode = upsideDown(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return leftNode
