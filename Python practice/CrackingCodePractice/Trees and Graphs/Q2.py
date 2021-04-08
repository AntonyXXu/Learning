#BST from Array
#linked List at depths

x = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
y = [-12, 11, 0, -5, 7, 11, 6, -7, 5, -3, -6]
z = [-12, -7, -6, -5, -3, 0, 5, 6, 11]

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            self.size += 1
            return 
        else:
            curr = self.root
            if self._insert(val, curr):
                self.size+=1
            return

    def _insert(self, val, node):
        while True:
            if val == node.val:
                return False
            elif val < node.val:
                if not node.left:
                    node.left = Node(val)
                    return True
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(val)
                    return True
                else:
                    node = node.right
    
    def inorder(self):
        self._inorder(self.root, 1)
    def _inorder(self, node, lev):
        if not node:
            return
        self._inorder(node.left, lev+1)
        print(node.val, lev)
        self._inorder(node.right, lev+1)

    def mintree(self, arr, low, high):
        if low > high:
            return
        mid = (low + high)//2
        self.insert(arr[mid])
        self.mintree(arr, low, mid - 1)
        self.mintree(arr, mid+1, high)

t = Tree()
t.mintree(z, 0, len(z)-1)
t.inorder()