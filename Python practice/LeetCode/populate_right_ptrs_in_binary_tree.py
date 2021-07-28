# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect( root: 'Node') -> 'Node':
    if not root:
        return root
    nextL = None
    if root.left and root.right:
        root.left.next = root.right
        nextL = root.left
    elif root.left:
        nextL = root.left
    elif root.right:
        nextL = root.right
    else:
        return root
    while nextL:
        current = nextL
        nextL = None
        prevN = None
        while current:
            if current.left:
                if prevN:
                    prevN.next = current.left
                    prevN = prevN.next
                else:
                    prevN = current.left
                    nextL = current.left
            if current.right:
                if prevN:
                    prevN.next = current.right
                    prevN = prevN.next
                else:
                    prevN = current.right
                    nextL = current.right
            current = current.next
    return root

n = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
t = connect(n)
        
