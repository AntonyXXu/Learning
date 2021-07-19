# https://leetcode.com/problems/partition-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    left = ListNode()
    right = ListNode()
    left_head = left
    right_head = right
    ptr = head
    while ptr:
        if ptr.val < x:
            left.next = ptr
            left = left.next
        else:
            right.next = ptr
            right = right.next
        ptr = ptr.next
    right.next = None
    left.next = right_head.next
    return left_head.next
