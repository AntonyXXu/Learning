# Rank from Stream
arr = [5, 1, 4, 4, 5, 9, 7, 13, 3]

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.smaller = 0

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        if self.size == 0:
            self.root = Node(val)
            self.size += 1
            return
        currNode = self.root
        self._insert(currNode, val)
        self.size += 1
        
    def _insert(self, node, val):
        if val > node.val:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = Node(val)
        elif val < node.val:
            node.smaller+=1
            if node.left:
               self._insert(node.left, val)
            else:
                node.left = Node(val)
        else:
            return

    def getRank(self, val):
        if not self.root:
            return -1
        curr = self.root
        return self._counter(curr, val)
    
    def _counter(self, curr, val):
        if not curr:
            return -1
        if curr.val == val:
            return 0
        if val < curr.val:
            res = self._counter(curr.left, val)
        else:
            res = self._counter(curr.right, val) + curr.smaller + 1
        return -1 if res == -1 else res

    def preorder(self):
        node = self.root
        self._preorder(node)
        print()
    def _preorder(self, node):
        if not node:
            return
        print(node.val, end = "\t")
        self._preorder(node.left)
        self._preorder(node.right)

    def inorder(self):
        node = self.root
        self._inorder(node)
        print()
    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        print(node.val, node.smaller, end = "\t")
        self._inorder(node.right)


b = BST()
for num in arr:
    b.insert(num)
b.inorder()

print(b.getRank(1))