class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

r = Node(5)
r.left = Node(4)
r.left.left = Node(3)
r.left.left.left = Node(2)
r.left.left.left.left = Node(1)
r.right = Node(6)

def traverse(node, arr):
    if not node:
        return
    traverse(node.left, arr)
    arr.append(node.val)
    traverse(node.right, arr)

def build(arr, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    node = Node(arr[mid])
    node.left = build(arr, low, mid - 1)
    node.right = build(arr, mid + 1, high)
    return node 

def bal(root):
    arr = []
    curr = root
    traverse(curr, arr)
    r = build(arr, 0, len(arr)-1)
    return r

def show(node):
    if not node:
        return
    show(node.left)
    print(node.val)
    show(node.right)


show(bal(r))
print(bal(r).val)
print(bal(r).left.val)
print(bal(r).right.val)