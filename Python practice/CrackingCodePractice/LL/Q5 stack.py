class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
x = Node(1)
x.next = Node(2)
x.next.next = Node(3)

y = Node(4)
y.next = Node(5)
y.next.next = Node(6)
y.next.next.next = Node(8)

def addTwo(x, y):
    xStack = []
    yStack = []
    ansHead = Node(None)
    ptr = Node(None)
    while x:
        xStack.append(x.val)
        x = x.next
    while y:
        yStack.append(y.val)
        y = y.next
    add = 0
    while xStack or yStack or add:
        val = add
        if xStack:
            val += xStack.pop()
        if yStack:
            val += yStack.pop()
        add = val // 10
        val = val % 10
        ptr.val = val
        ansHead = Node(None, ptr)
        ptr = ansHead
    return ansHead.next

ans = addTwo(x,y)
while ans:
    print(ans.val)
    ans = ans.next