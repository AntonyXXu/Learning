# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    if not head:
        return head
    d = {}
    ptr = head
    while ptr:
        d[ptr] = Node(ptr.val)
        ptr = ptr.next

    ptr = head
    while ptr:
        if not ptr.next:
            d[ptr].next = None
        else:
            d[ptr].next = d[ptr.next]
        if not ptr.random:
            d[ptr].random = None
        else:
            d[ptr].random = d[ptr.random]
        ptr = ptr.next
    return d[head]