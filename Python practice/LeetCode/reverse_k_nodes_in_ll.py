# https://leetcode.com/problems/reverse-nodes-in-k-group/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k):
    if k == 1:
        return head
    dummy = ListNode(0, head)
    pre = dummy
    left = right = head
    while right:
        ctr = 0
        while ctr < k and right:
            ctr += 1
            right = right.next
        if ctr == k:
            prev = right
            curr = left
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            pre.next = prev
            pre = left
            left = right
        else:
            return dummy.next
    return dummy.next
