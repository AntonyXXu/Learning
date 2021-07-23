# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
def zigzagLevelOrder(root):
    if not root:
        return []
    res = []
    dq = collections.deque()
    dq.append(root)
    currLevel = 0
    while dq:
        levelArr = []
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
            levelArr.append(curr.val)
        if currLevel % 2 == 1:
            levelArr.reverse()
        res.append(levelArr)
        currLevel += 1
    return res

r = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(zigzagLevelOrder(r))
