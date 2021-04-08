class LinkedListNode:
    def __init__(self, val, nextVal=None):
        self.val = val
        self.next = nextVal

x = LinkedListNode(1)
x.next = LinkedListNode(2)
x.next.next = LinkedListNode(3)

y = LinkedListNode(4)
y.next = LinkedListNode(5)
y.next.next = LinkedListNode(6)
y.next.next.next = LinkedListNode(8)

def sumList(x, y):
    ansHead = None
    ans = ansHead
    carry = 0
    while x or y:
        val = carry
        if x:
            val+=x.val
            x=x.next
        if y:
            val+=y.val
            y = y.next
        carry = val // 10
        val = val % 10
        if not ansHead:
            ansHead = LinkedListNode(val)
            ans = ansHead
        else:
            ans.next = LinkedListNode(val)
            ans = ans.next
    #ans.next = None
    return ansHead
        
ans = sumList(x, y)
while ans:
    print(ans.val)
    ans=ans.next


