# https://leetcode.com/problems/binary-search-tree-iterator/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.buildStk(root)
        self.index = 0

    def buildStk(self, root):
        if not root:
            return
        self.buildStk(root.left)
        self.stk.append(root)
        self.buildStk(root.right)

    def next(self) -> int:
        returnV = self.stk[self.index]
        self.index += 1
        return returnV.val

    def hasNext(self) -> bool:
        return self.index < len(self.stk)


s = BSTIterator(TreeNode(0))
print(s.hasNext())
print(s.next())
print(s.hasNext())
