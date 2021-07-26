# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    indexes = {}
    for i, v in enumerate(inorder):
        indexes[v] = i
    left = 0
    right = len(inorder) - 1
    return build( postorder, left, right, indexes)

def build(postorder, left, right, indexes):
    if not postorder:
        return None
    val = postorder.pop()
    root = TreeNode(val)
    inorderIndex = indexes[val]
    root.left = build(postorder, left, inorderIndex - 1, indexes)
    root.right = build(postorder, inorderIndex + 1, right, indexes)
    return root