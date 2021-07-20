# https://leetcode.com/problems/reverse-linked-list-ii/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left >= right:
        return head
    dummy = ListNode()
    dummy.next = head
    while left > 1:
        head = head.next
        left -= 1
        right -= 1
    tail = head.next
    while right > 1:
        next = head.next
        head.next = tail.next
        tail.next = tail.next.next
        head.next.next = next
        

    

    return dummy.next



h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
x = reverseBetween(h1, 2, 4)
print(x.next.val)
# while reverseBetween(h1, 2, 4):
#     print(h1.val)
#     h1 = h1.next