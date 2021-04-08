class Node:
    def __init__(self, val, nextv=None):
        self.val = val
        self.next = nextv

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
y.next.next.next.next.next.next.next = Node(1)
def reverse(x):
    if x == None:
        return False
    currNode = x
    newHead = None
    newPtr = None
    while currNode:
        newHead = Node(currNode.val, newPtr)
        newPtr = newHead
        currNode = currNode.next
    return newHead

def pd(LL):
    if LL == None:
        return False
    rev = reverse(LL)
    pallindrome = True
    while rev and LL and pallindrome:
        if rev.val != LL.val:
            pallindrome = False
        rev = rev.next
        LL = LL.next
    return pallindrome

print(pd(y))
