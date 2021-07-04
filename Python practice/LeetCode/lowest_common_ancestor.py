# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcaDeepestLeaves(root: TreeNode):
    depth, node = checker(root) 
    return node

def checker(node):
    if not node:
        return 0, node
    lh, left = checker(node.left)
    rh, right = checker(node.right)
    if lh == rh:
        return lh + 1, node
    elif lh > rh:
        return lh + 1, left
    else:
        return rh + 1, right
    
