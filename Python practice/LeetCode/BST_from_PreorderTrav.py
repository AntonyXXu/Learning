# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), 
# construct the tree and return its root.

ex  = [8,5,1,7,10,12]
ex1 = [1,3]

class Node:
    def __init__(self, val, left= None, right = None):
        self.val = val
        self.right = right
        self.left = left

def build_preorder(arr):
    if not arr or len(arr) == 0:
        return None
    root, i = helper(arr, 0, arr[len(arr)-1])
    return root

def helper(arr, i, maxval):
    if i >= len(arr) or arr[i] > maxval:
        return None, i
    node = Node(arr[i])
    i += 1
    node.left, i = helper(arr, i, node.val)
    node.right, i = helper(arr, i, maxval)
    return node, i



r = build_preorder(ex)
print(r.val)