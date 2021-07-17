# https://leetcode.com/problems/rotate-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateList(head, k):
    if not head:
        return head
    length = 1
    traverse = head
    while traverse.next:
        length += 1
        traverse = traverse.next
    rotate = k % length
    traverse.next = head
    headPtr = head 
    for i in range(length - rotate - 1):
        headPtr = headPtr.next
    returnVal = headPtr.next 
    headPtr.next = None
    return returnVal

h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
h2 = ListNode(0, ListNode(1, ListNode(2)))
h3 = ListNode(1, ListNode(2))
def printAll(head):
    while head:
        print(head.val)
        head = head.next

printAll(rotateList(h1, 0))
# printAll(rotateList(h2, 4))
printAll(rotateList(h3, 1))