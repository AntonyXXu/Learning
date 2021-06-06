class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insert(val, root):
    curr = root
    _insert(val, curr)
    return root

def _insert(val, node):
    if not node:
        node = Node(val)
        return node
    if val == node.val:
        return node
    elif val < node.val:
        node.left = _insert(val, node.left)
    else:
        node.right = _insert(val, node.right)
    return node

n= Node(5)
n.left = Node(3)
n.left.left = Node(1)
n.left.right = Node(4)
n.right = Node(8)
n.right.right = Node(15)

insert(10, n)
print(n.right.right.left.val)
insert(7, n)
print(n.right.left.val)