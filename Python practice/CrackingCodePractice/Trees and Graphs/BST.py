class Node:
    def __init__(self, val, left= None, right= None, parent= None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None
        self.size = 0