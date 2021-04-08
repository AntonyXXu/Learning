class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse(Nodehead):
    n = Nodehead
    new = Node(None)
    newHead = Node(None)
    while n:
        new.val = n.val
        newHead = Node(None, new)
        new = newHead
        n = n.next
    return newHead.next

y = Node(4)
y.next = Node(5)
y.next.next = Node(6)
y.next.next.next = Node(8)

x = reverse(y)
while x:
    print(x.val)
    x = x.next



    

