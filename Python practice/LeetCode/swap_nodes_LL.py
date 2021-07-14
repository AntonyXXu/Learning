# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodePairs(head):
    if not head or not head.next:
        return head
    temp = head.next
    head.next = temp.next
    temp.next = head
    prev = head
    returnNode = temp
    fwd = temp.next.next
    while fwd and fwd.next:
        head = fwd
        temp = head.next
        head.next = temp.next
        temp.next = head
        prev.next = temp
        prev = head
        fwd = temp.next.next

    return returnNode

h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
h1 = swapNodePairs(h)
while h1:
    print(h1.val)
    h1 = h1.next