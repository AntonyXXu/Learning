class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

l1 = Node(0)
l1.next = Node(1)
l1.next.next = Node(2)
l1.next.next.next = Node(3)
l1.next.next.next.next = Node(4)
l1.next.next.next.next.next = Node(5)
l2 = Node(10)
l2.next = Node(11)
l2.next.next = Node(12)

def merge(l1, a, b, l2):
    if b < a:
        return l1
    l1_h = l1
    runner = l2
    while runner.next:
        runner = runner.next
    l2_tail = runner

    runner = l1
    a_head = None
    i = 0
    while i < b:
        if i == a-1:
            a_head = runner
        runner = runner.next
        i += 1
    b_tail = runner
    if a == 0:
        l2_tail.next = b_tail.next
        return l2
    else:
        a_head.next = l2
        l2_tail.next = b_tail.next
        b_tail.next = None
        return l1_h

h = merge(l1, 5, 5, l2)
while h:
    print(h.val)
    h = h.next