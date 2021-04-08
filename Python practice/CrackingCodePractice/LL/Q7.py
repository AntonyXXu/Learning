class Node:
    def __init__(self, val, nextv= None):
        self.val = val
        self.next = nextv

y = Node(1)
y.next = Node(2)
y.next.next = Node(3)
# y.next.next.next = Node(4)
# y.next.next.next.next = Node(5)
# y.next.next.next.next.next = Node(6)
# y.next.next.next.next.next.next = Node(7)
 
x = Node(10)
x.next = Node(20)
x.next = y.next.next


def intersect(x, y):
    if x is None or y is None:
        return None
    ptr1 = x
    ptr2 = y
    while ptr1 is not ptr2:
        if not ptr1:
            ptr1 = y
        else:
            ptr1 = ptr1.next
        if not ptr2:
            ptr2 = x
        else:
            ptr2 = ptr2.next
    return ptr1

ans = intersect(x,y)
try:
    print(ans.val)
except:
    print(ans)

# print(ans.val)
