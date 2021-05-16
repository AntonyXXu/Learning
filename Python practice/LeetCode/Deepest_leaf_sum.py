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

def deepestSumQueue(root):
    if not root:
        return 0
    total = 0
    q = [root]
    while len(q):
        total = 0
        for i in range(len(q)):
            curr = q[0]
            q.pop(0)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            else:
                total += curr.val
    return total
    
            
