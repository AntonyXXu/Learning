# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.index = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        left = self.kthSmallest(root.left, k)
        if left is not None:
            return left
        self.index += 1
        if self.index == k:
            return root.val
        right = self.kthSmallest(root.right, k)
        if right is not None:
            return right


t = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
s = Solution()
print(s.kthSmallest(t, 1))
