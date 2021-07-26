# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottomUp(root):
    if not root:
        return None
    dq = collections.deque()
    dq.append(root)
    res = []
    while dq:
        level = []
        for _ in range(len(dq)):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            level.append(node.val)
        res.append(level)
    return reversed(res)