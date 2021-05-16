# Given the root of a binary tree, return the sum of values of its deepest leaves.

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right= right

deepest = 0
sum = 0
def deepestSum(root):
    sum = 0
    deepest = 0
    helper(root, 0)
    return sum
    

def helper(node, level):
    if not node:
        return 0
    if level > deepest:
        deepest = level
        sum = 0
    if level == deepest:
        sum += node.val
    helper(node.left, level+1)
    helper(node.right, level+1)

