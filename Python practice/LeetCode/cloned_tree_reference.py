# Given two binary trees original and cloned and given a reference to a node target in the original tree.

# The cloned tree is a copy of the original tree.

# Return a reference to the same node in the cloned tree.

# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

# Follow up: Solve the problem if repeated values on the tree are allowed.

class TNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def searchCopy(orig_head, copy_head, targetNode):
    oh = orig_head
    ch = copy_head
    return search(oh, ch, targetNode)

def search(origNode, copyNode, targetNode):
    if not origNode:
        return
    if targetNode == origNode:
        return copyNode
    left = search(origNode.left, copyNode.left, targetNode)
    if left:
        return left
    right = search(origNode.right, copyNode.right, targetNode)
    if right:
        return right

ohead = TNode(7)
chead = TNode(7)
x = searchCopy(ohead, chead, ohead)
print(x == chead)
ohead.left = TNode(4)
chead.left = TNode(4)
ohead.right = TNode(3)
chead.right = TNode(3)
x = searchCopy(ohead.right, chead.right, ohead.right)
print(x == chead.right)