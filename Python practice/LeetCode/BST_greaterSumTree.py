# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST 
# is changed to the original key plus sum of all keys greater than the original key in BST.

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = Node(4)
root.left = Node(1)
root.left.left = Node(0)
root.left.right = Node(2)
root.left.right.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)

def convertToGreatestSum(root):
    curr = root
    total = [0]
    inOrder(curr, total)

def inOrder(node, total):
    if not node:
        return
    inOrder(node.right, total)
    total[0] += node.val
    node.val = total[0]
    inOrder(node.left, total)

convertToGreatestSum(root)

print(root.right.right.right.val, root.left.val, root.left.left.val, root.val)