class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
r1 = Node(5)
r1.left = Node(3)
r1.left.left = Node(2)
r1.left.right = Node(4)
r1.right = Node(10)
r1.right.left = Node(8)
r1.right.right = Node(15)
r1.right.right.left = Node(12)

def inOrder(root):
    stk = []
    node = root
    while True:
        while node:
            stk.append(node)
            node = node.left
        node = stk.pop()
        print(node.val, end="\t")
        node = node.right
        if not node and not len(stk):
            print()
            break
    return

inOrder(r1)