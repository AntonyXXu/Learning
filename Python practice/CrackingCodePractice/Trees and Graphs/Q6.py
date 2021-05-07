
#Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.

def findNext(node):
    current = node
    if current.right:
        current = current.right
        while current.left:
            current = current.left
        return current
    else:
        while current.parent:
            if current.parent.val > current.parent:
                return current.parent
        return node
    


# def findNext(node):
#     current = node
#     if current.right:
#         current = current.right
#         while current.left:
#             current = current.left
#         return current
#     else:
#         while current.parent:
#             if current.parent.val > node.val:
#                 return current.parent
#         return node
