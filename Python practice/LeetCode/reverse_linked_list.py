# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    if not head:
        return head
    ptr = head
    prev = None
    while ptr:
        next = ptr.next
        ptr.next = prev
        prev = ptr
        ptr = next
    return prev