# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNth(head, n):
    ptr = head
    count = 0
    while ptr:
        count += 1
        ptr = ptr.next
    k = count - n
    ptr2 = head
    prev = None
    if k == 0:
        return ptr2.next

    for i in range(k):
        prev = ptr2
        ptr2 = ptr2.next
    
    prev.next = ptr2.next
    return head