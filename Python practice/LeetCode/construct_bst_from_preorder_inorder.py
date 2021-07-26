class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    if len(preorder) == 1 or len(inorder) == 1:
        return TreeNode(preorder[0])
    indexes = {}
    for i, v in enumerate(inorder):
        indexes[v] = i

    stk = []
    head = None
    for val in preorder:
        if not head:
            head = TreeNode(val)
            stk.append(head)
        else:
            currNode = TreeNode(val)
            if indexes[val] < indexes[stk[-1].val]:
                stk[-1].left = currNode
            else:
                while stk and indexes[stk[-1].val] < indexes[val]:
                    parent = stk.pop()
                parent.right = currNode
            stk.append(currNode)
    return head

def buildTree(preorder, inorder):
    if inorder:
        val = preorder.pop(0)
        index = inorder.index(val)
        root = TreeNode(val)
        root.left = buildTree(preorder, inorder[:index])
        root.right = buildTree(preorder, inorder[index+1:])
        return root