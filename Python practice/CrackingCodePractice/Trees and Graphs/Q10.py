#check subtree
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def inorder(nd):
    n = nd
    height = 0
    _order(n, height)
def _order(n, h):
    if not n:
        return
    _order(n.left, h+1)
    print(h, n.val)
    _order(n.right, h+1)

h1 = Node(10)
h1.left = Node(5)
h1.right = Node(15)
h1.left.left = Node(8)
h1.left.right = Node(18)
h1.right.left = Node(12)
h1.right.right = Node(21)
h1.right.right.left = Node(60)
h1.right.right.right = Node(51)
h2 = Node(10)

def check(r1, r2):
    if r2 == None:
        return True
    if r1 == None:
        return False
    ptr1 = r1
    ptr2 = r2
    if r1 == r2:
        if preorder_check(ptr1, ptr2):
            return True
        else:
            ptr1 = r1
            ptr2 = r2
    if check(ptr1.left, ptr2):
        return True
    if check(ptr1.right, ptr2):
        return True
    return False

def preorder_check(n1, n2):
    if not n1 and not n2:
        return True
    elif not n1 or not n2:
        return False
    elif n1 != n2:
        return False
    if not preorder_check(n1.left, n2.left):
        return False
    if not preorder_check(n1.right, n2.right):
        return False
    return True
inorder(h1)
print(check(h1, h2))