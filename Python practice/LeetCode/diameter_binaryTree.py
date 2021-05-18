# Given a binary tree, write an efficient algorithm to compute the diameter of it. 
# A binary tree diameter equals the total number of nodes on the longest path between any two leaves in it.

class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

def diameterTree(node):
    currNode = node
    temp, diameter = helper(currNode, 0)
    return diameter

def helper(node, diameter):
    if not node:
        return 0, diameter
    left, d1 = helper(node.left, diameter)
    right, d2 = helper(node.right, diameter)
    height = max(left, right) + 1
    diameter = left + right + 1
    diameter = max(diameter, d1, d2)
    return height, diameter    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(diameterTree(root))