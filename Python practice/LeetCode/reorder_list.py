# https://leetcode.com/problems/reorder-list/

def reorder(head):
    if not head or not head.next:
        return head

    # find middle
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # reverse
    prev = None
    curr = slow.next
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    slow.next = None

    # prev is h2
    # head is h1
    h1 = head
    h2 = prev
    while h1:
        nxt = h1.next
        h1.next = h2
        h1 = nxt
        temp = h2
        h2 = h2.next
        if not h1:
            temp.next = slow
        else:
            temp.next = h1
    return head
