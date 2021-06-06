# https://leetcode.com/problems/delete-leaves-with-a-given-value/

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def delete(root, target):
    n = root
    helper(None, n, target)
    return root

def helper(parent, node, target):
    if not node:
        return
    if node.left:
        helper(node, node.left, target)
    if node.right:
        helper(node, node.right, target)
    if not node.left and not node.right and node.val == target:
        if not parent:
            node = None
        else:
            if node == parent.left:
                parent.left = None
            else:
                parent.right = None
        

n = Node(1)
n.left = Node(2)
n.left.left = Node(2)
n.left.left.right = Node(1)

r = delete(n,2)
print(n.val)
print(n.left.left.right.val)