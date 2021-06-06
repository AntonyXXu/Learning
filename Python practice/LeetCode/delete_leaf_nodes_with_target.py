# https://leetcode.com/problems/delete-leaves-with-a-given-value/

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

def delete(root, target):
    n = root
    newR = helper(None, n, target)
    return newR

def helper(parent, node, target):
    if not node:
        return None
    node.left = helper(node, node.left, target)
    node.right = helper(node, node.right, target)
    if not node.left and not node.right and node.val == target:
        return None
    return node
        

n = Node(2)
n.left = Node(2)
n.left.left = Node(2)
n.left.left.right = Node(2)

r = delete(n,2)
print(r)