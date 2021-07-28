# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    if not root:
        return None
    if root.left:
        root.left.next = root.right
    if root.right and root.next:
        root.right.next = root.next.left
    connect(root.left)
    connect(root.right)
    return root

def connectIt(root):
    if not root:
        return None
    start = root
    while start:
        current = start
        while current:
            if current.left:
                current.left.next = current.right
            if current.right and current.next:
                current.right.next = current.next.left
            current = current.next
        
        start = start.left
    return root