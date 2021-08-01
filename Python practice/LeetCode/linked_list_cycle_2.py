# https://leetcode.com/problems/linked-list-cycle-ii/
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    if not head:
        return None
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return slow


l = ListNode(3)
l.next = ListNode(2)
l.next.next = ListNode(0)
l.next.next.next = ListNode(4)
l.next.next.next.next = l.next

print(detectCycle(l).val)
