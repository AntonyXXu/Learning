x = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
y = [-12, 11, 0, -5, 7, 11, 6, -7, 5, -3, -6]
z = [-12, -7, -6, -5, -3, 0, 5, 6, 11]

# class Node:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Tree:
#     def __init__(self):
#         self.root = None
#         self.size = 0

#     def insert(self, val):
#         if not self.root:
#             self.root = Node(val)
#             self.size += 1
#             return 
#         else:
#             curr = self.root
#             if self._insert(val, curr):
#                 self.size+=1
#             return

#     def _insert(self, val, node):
#         while True:
#             if val == node.val:
#                 return False
#             elif val < node.val:
#                 if not node.left:
#                     node.left = Node(val)
#                     return True
#                 else:
#                     node = node.left
#             else:
#                 if not node.right:
#                     node.right = Node(val)
#                     return True
#                 else:
#                     node = node.right
    
#     def inorder(self):
#         self._inorder(self.root, 1)
#     def _inorder(self, node, lev):
#         if not node:
#             return
#         self._inorder(node.left, lev+1)
#         print(node.val, lev)
#         self._inorder(node.right, lev+1)

#     def mintree(self, arr, low, high):
#         if low > high:
#             return
#         mid = (low + high)//2
#         self.insert(arr[mid])
#         self.mintree(arr, low, mid - 1)
#         self.mintree(arr, mid+1, high)

#     def depthslists(self):
#         if not self.root:
#             return None
#         result = []
#         ptr = self.root
#         level = 1
#         self._traverse_depth(ptr, result, level)
#         return result
#     def _traverse_depth(self, ptr, result, level):
#         if not ptr:
#             return
#         if len(result) < level:
#             result.append(LL())
#         result[level-1].insert(ptr.val)
#         self._traverse_depth(ptr.left, result, level + 1)
#         self._traverse_depth(ptr.right, result, level + 1)
    
# class N:
#     def __init__(self, val, nextv = None):
#         self.val = val
#         self.next = nextv
# class LL:
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def insert(self, val):
#         if not self.head:
#             self.head = N(val)
#         else:
#             curr = self.head
#             while curr.next:
#                 curr = curr.next
#             curr.next = N(val)
#             self.size+=1

# t = Tree()
# t.mintree(z, 0, len(z)-1)

# print(t.depthslists())

# for lst in t.depthslists():
#     temp = lst.head
#     while temp:
#         print(temp.val, end = "\t")
#         temp = temp.next
#     print("")
