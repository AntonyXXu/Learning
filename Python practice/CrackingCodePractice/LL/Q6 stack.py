class Node:
    def __init__(self, val, nextv=None):
        self.val = val
        self.next = nextv

y = Node(1)
y.next = Node(2)
y.next.next = Node(3)
y.next.next.next = Node(4)
y.next.next.next.next = Node(3)
y.next.next.next.next.next = Node(2)
y.next.next.next.next.next.next = Node(1)
#y.next.next.next.next.next.next.next = Node(0)

def pallindrome(y):
    if y == None:
        return False
    fast = slow = y
    valStack = []
    p = True
    while fast and fast.next:
        valStack.append(slow.val)
        fast = fast.next.next
        slow = slow.next
    if fast:
        slow = slow.next
    while slow and p:
        if slow.val == valStack.pop():
            slow = slow.next
        else:
            p = False

    return p
    

print(pallindrome(y))