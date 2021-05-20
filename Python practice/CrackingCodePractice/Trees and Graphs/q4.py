#check balance
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class LL:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            return True
        ptr = self.root
        while True:
            if ptr.val == val:
                return True
            elif ptr.val > val:
                if ptr.left:
                    ptr = ptr.left
                else:
                    ptr.left = Node(val)
            else:
                if ptr.right:
                    ptr = ptr.right
                else:
                    ptr.right = Node(val)
    def inorder(self):
        curr = self.root
        self._inorder(self.root, 1)
    def _inorder(self, curr, level):
        if not curr:
            return
        self._inorder(curr.left, level+1)
        print(level, curr.val)
        self._inorder(curr.right, level+1)

    # def check(self):
    #     level = 0
    #     current = self.root
    #     return self._check(current, level)

    # def _check(self, current, level):
    #     if not current:
    #         return level
    #     leftL = self._check(current.left, level+1)
    #     if leftL < 0:
    #         return -1
    #     rightL = self._check(current.right, level+1)
    #     if rightL < 0:
    #         return -1
    #     if abs(leftL - rightL) > 1:
    #         return -1
    #     return max(leftL, rightL)


    def check(self):
        node = self.root
        height = self._check(node)
        return -1 if height < 0 else height

    def _check(self, node):
        if not node:
            return 0
        leftH = self._check(node.left) + 1
        if leftH < 0:
            return -2
        rightH = self._check(node.right) + 1
        if rightH < 0:
            return -2
        if abs(rightH - leftH) <= 1:
            return max(leftH, rightH)
        return -2


x = [i*i for i in range(10)]
lst = LL()
def mintree(arr, tree, low, high):
    if low > high:
        return
    mid = (low + high)//2
    lst.insert(arr[mid])
    mintree(arr, tree, low, mid-1)
    mintree(arr, tree, mid+1, high)


mintree(x, lst, 0, len(x)-1)
lst.insert(-1)
lst.insert(-5)
lst.insert(0.5)
lst.insert(-10)
lst.insert(-15)
lst.inorder()

print(lst.check())