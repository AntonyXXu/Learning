# https://leetcode.com/problems/binary-tree-level-order-traversal/

def levelOrder(root):
    res = []
    level = 0
    trav(root, level, res)
    return res

def trav(node, level, res):
    if not node:
        return 
    if level > len(res) - 1:
        res.append([])
    res[level].append(node.val)
    trav(node.left, level + 1, res)
    trav(node.right, level + 1, res)

import collections
def levelOrder(root):
    if not root:
        return []
    dq = collections.deque()
    dq.append(root)
    res = []
    while dq:
        level = []
        for _ in range(len(dq)):
            curr = dq.popleft()
            level.append(curr.val)
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
        res.append(level)
    return res