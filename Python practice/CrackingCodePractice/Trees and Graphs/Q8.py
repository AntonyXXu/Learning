#First Common Ancestor, not necessarily a BST
#without additional data struct

class Node:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
def inorder(root):
    temp = root
    height = -1
    pinorder(temp, height+1)
def pinorder(node, height):
    if not node:
        return
    pinorder(node.left, height+1)
    print(height, node.val )
    pinorder(node.right, height+1)

testH = Node(1)
runner = testH
runner.left = Node(3, parent = runner)
runner.right = Node(2, parent = runner)
runner = runner.left
runner.left = Node(37, parent = runner)
runner.right = Node(6, parent = runner)
y = runner.right
runner = runner.left
runner.left = Node(0, parent = runner)
x = runner.left
runner = testH.right
runner.left = Node(50, parent = runner)
runner.right = Node(9, parent = runner)
z = runner.left
inorder(testH)
    
def common(node1, node2):
    r1 = node1
    r2 = node2
    while r1 != r2:
        r1 = r1.parent
        r2 = r2.parent
        if r1 == None:
            r1 = node2
        if r2 == None:
            r2 = node1
    return r1

print(common(z,x).val)

#without parent
def com(root, node1, node2):
    if not root:
        return None
    #checker helper
    curr = root
    return checker(curr, node1, node2)

def checker(curr, node1, node2):
    if not curr:
        return False
    if curr == node1 or curr == node2:
        return curr
    test1 = find(curr.left, node1)
    test2 = find(curr.left, node2)
    if test1 != test2:
        return curr
    elif test1 == True:
        return checker(curr.left, node1, node2)
    else:
        return checker(curr.right, node1, node2)

def find(curr, node):
    if not curr:
        return False
    if node == curr:
        return True
    return find(curr.left, node) or find(curr.right, node)

print(com(testH, x,z).val)