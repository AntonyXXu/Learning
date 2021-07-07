class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.right:
        return min_depth(root.left) + 1
    if not root.left:
        return min_depth(root.right) + 1
    else:
        left = min_depth(root.left)
        right = min_depth(root.right)
        return min(left, right) + 1

n = Node(3)
n.left = Node(9)
n.right = Node(20)
n.right.right = Node(7)
n.right.left = Node(15)
s = Node(1)
s.right = Node(1)
s.right.right=Node(1)
s.right.right.right= Node(1)

print(min_depth(n))
print(min_depth(s))
print(min_depth(None))