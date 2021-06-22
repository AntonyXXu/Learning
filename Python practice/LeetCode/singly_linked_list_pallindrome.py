class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pallindrome(head):
    # get mid
    slow = head
    fast = head
    inverse = None
    while fast and fast.next:
        fast = fast.next.next
        # Reverse
        inverse, inverse.next, slow = slow, inverse, slow.next

    midHead = slow
    inverseTraverse = inverse

    if fast:
        slow = slow.next
    ans = True
    while slow and inverseTraverse:
        if slow.val != inverseTraverse.val:
            ans = False
            break
        slow = slow.next
        inverseTraverse = inverseTraverse.next
    
    while inverse:
        midHead, midHead.next, inverse = inverse, midHead, inverse.next
    return ans

def isPalindrome(head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

x = Node(1)
x.next = Node(2)
x.next.next = Node(3)

y = Node(1)
y.next = Node(2)
y.next.next = Node(3)
y.next.next.next = Node(4)
y.next.next.next.next = Node(3)
y.next.next.next.next.next = Node(2)
y.next.next.next.next.next.next = Node(1)
# y.next.next.next.next.next.next.next = Node(1)

print(pallindrome(x))
print(pallindrome(y))