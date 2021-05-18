# Given a binary tree, return the sum of values of nodes with even-valued grandparent.  
# (A grandparent of a node is the parent of its parent, if it exists.)

# If there are no nodes with an even-valued grandparent, return 0.

# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def EvenGrandParentSum(root):
    currentNode = root
    ctr1 = -1
    ctr2 = -1
    return helper(currentNode, ctr1, ctr2)
    
def helper(node, ctr1, ctr2):
    if not node:
        return 0
    inc = 0
    if ctr1 == 0 or ctr2 == 0:
        inc = node.val
    if node.val % 2 == 0:
        if ctr1 <= 0:
            ctr1 = 2 
        elif ctr2 <= 0:
            ctr2 = 2
    left = helper(node.left, ctr1-1, ctr2-1)
    right = helper(node.right,  ctr1-1, ctr2-1)
    return left + right + inc

r = Node(6)
r.left = Node(7)
r.right = Node(8)
r.left.left = Node(2)
r.left.right = Node(7)
r.left.left.left = Node(9)
r.left.right.left = Node(1)
r.left.right.right = Node(4)
r.right.left = Node(1)
r.right.right = Node(3)
r.right.right.right = Node(5)

print(EvenGrandParentSum(r))