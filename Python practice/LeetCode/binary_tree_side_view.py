# https://leetcode.com/problems/binary-tree-right-side-view/
# Definition for a binary tree node.
import collections


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


def level(root):
    if not root:
        return []
    ans = []
    dq = collections.deque()
    dq.append(root)
    while dq:
        curr = None
        for _ in range(len(dq)):
            curr = dq.popleft()
            if curr.left:
                dq.append(curr.left)
            if curr.right:
                dq.append(curr.right)
        ans.append(curr.val)
    return ans
