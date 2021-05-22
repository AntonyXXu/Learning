class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

r1 = Node(2, Node(1), Node(4))
r2 = Node(1, Node(0), Node(3))

r3 = None
r4 = Node(5, Node(1, Node(0), Node(2)), Node(7))

def toArray(r1, r2):
    res1 = []
    res2 = []
    n1 = r1
    n2 = r2
    helper(res1, n1)
    helper(res2, n2)
    print(res1)
    print(res2)
    i = 0
    j = 0
    res = []
    while i < len(res1) and j < len(res2):
        if res1[i] <= res2[j]:
            res.append(res1[i])
            i += 1
        else:
            res.append(res2[i])
            j += 1
    res.extend(res1[i:])
    res.extend(res2[j:])
    return res

def helper(arr, root):
    if not root:
        return
    helper(arr, root.left)
    arr.append(root.val)
    helper(arr, root.right)

print(toArray(r1,r2))
print(toArray(r4,r3))