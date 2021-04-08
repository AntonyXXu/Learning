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

def reverse(nodeHead):
    currNode = nodeHead
    tempNode = Node(None)
    newHead = Node(None)
    while currNode:
        tempNode.val = currNode.val
        newHead = Node(None, tempNode)
        tempNode = newHead
        currNode = currNode.next
    return newHead.next

newX = reverse(x)
newY = reverse(y)

def addTwo(x, y):
    ansHead = None
    ansPtr = None
    add = 0
    val = 0
    while x or y:
        if y:
            val += y.val
            y = y.next
        if x:
            val += x.val
            x = x.next
        add = val // 10
        val = val % 10
        if not ansHead:
            ansHead = Node(val)
            ansPtr = ansHead
        else:
            ansPtr.next = Node(val)
            ansPtr = ansPtr.next
        val = add
    return ansHead

ans = addTwo(newX, newY)
ans = reverse(ans)

while ans:
    print(ans.val)
    ans = ans.next








