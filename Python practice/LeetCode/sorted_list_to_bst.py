# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def buildTree(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)
    sortedList = []
    while head:
        sortedList.append(head.val)
        head = head.next
    return dfs(0, len(sortedList)-1, sortedList)

def dfs(left, right, sortedList):
    if left > right:
        return None
    mid = (left + right) // 2
    root = TreeNode(sortedList[mid])
    root.left = dfs(left, mid - 1, sortedList)
    root.right = dfs(mid + 1, right, sortedList)
    return root

def buildTreeInorder(head):
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = None
    root = TreeNode(slow.val)
    root.left = buildTreeInorder(head)
    root.right = buildTreeInorder(slow.next)
    return root



