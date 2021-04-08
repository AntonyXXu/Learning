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

    def check(self):
        ptr = self.root
        res = self._check(ptr, 1)
        return res

    def _check(self, ptr, level):
        if not ptr:
            return level - 1
        left = self._check(ptr.left, level+1)
        if left < 0:
            return -1
        right = self._check(ptr.right, level+1)
        if right < 0:
            return -1
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right)


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
# lst.insert(-1)
# lst.insert(-5)
lst.insert(0.5)
lst.insert(-10)
lst.insert(-15)
lst.inorder()

print(lst.check())