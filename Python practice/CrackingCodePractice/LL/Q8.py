class Node:
    def __init__(self, val, nextv = None):
        self.val = val
        self.next = nextv
    
y = Node(1)
y.next = Node(2)
y.next.next = Node(3)
y.next.next.next = Node(4)
y.next.next.next.next = Node(5)
y.next.next.next.next.next = y.next.next.next

def getLoopSet(x):
    currNode = x
    setN = set()
    loop = False
    while not loop and currNode:
        if currNode in setN:
            return currNode
        setN.add(currNode)
        currNode = currNode.next
    return None

def getLoopRunner(x):
    slow = x
    fast = x
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slowHead = x
            while slowHead is not slow:
                slow = slow.next
                slowHead = slowHead.next
            return slow
    return None


# x = getLoopSet(y)
x = getLoopRunner(y)

try:
    print(x.val)
except:
    print(x)