# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDup(head):
    if not head or not head.next:
        return head
    dummy = ListNode(None)
    dummy.next = head
    prev = dummy
    ptr = head
    while ptr and ptr.next:
        if ptr.val == ptr.next.val:
            while ptr and ptr.next and ptr.val == ptr.next.val:
                ptr = ptr.next
            if not ptr.next:
                prev.next = None
                return dummy.next
            prev.next = ptr.next
            ptr = ptr.next
        else:
            prev = ptr
            ptr = ptr.next
    return dummy.next