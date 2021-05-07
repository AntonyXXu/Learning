#validate bst

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

    def validate(self):
        node = self.root
        val = None
        return self.helper(node, val)
    
    def helper(self, node, val):
        if not node:
            return True
        if not self.helper(node.left, val):
            return False
        if not val or val <= node.val:
            val = node.val
        else:
            return False
        if not self.helper(node.right, val):
            return False
        return True



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
# lst.root.right.val = 6

lst.inorder()

print(lst.validate())