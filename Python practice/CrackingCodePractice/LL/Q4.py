class Node:
    def __init__(self, val, nextVal = None):
        self.val = val 
        self.next = nextVal

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def showList(self):
        curr = self.head
        while curr:
            print(curr.val, end = " ")
            curr = curr.next

    def insertfront(self, val):
        temp = Node(val, self.head)
        self.head = temp
        self.size+=1
    
    def insert(self, val, index):
        if index < 0 or index > self.size-1:
            return -1
        currNode = self.head
        i = 0
        while currNode:
            if i == index:
                currNode = currNode.next
                i+=1
        currNode.next = Node(val, currNode.next)
        return index
    
    def delete(self, index):
        if index < 0 or index > self.size - 1:
            return -1
        if index == 0:
            self.head = self.head.next
            self.size -=1 
        else:
            currNode = self.head
            prevNode = None
            while index > 0:
                prevNode = currNode
                currNode = currNode.next
                index -= 1
            prevNode.next = currNode.next
            self.size-=1
        return index

LL = LinkedList()
for i in range(6):
    LL.insertfront(i)
#LL.insert("t",1)

def partitionLL(head, x):
    leftHead = Node(None)
    rightHead = Node(None)
    left = Node (None)
    right = Node (None)
    currentNode = head
    while currentNode:
        if currentNode.val < x:
            if not leftHead.val:
                leftHead = currentNode
                left = leftHead
            else:
                left.next = currentNode
                left = left.next
        else:
            if not rightHead.val:
                rightHead = currentNode
                right = rightHead
            else:
                right.next = currentNode
                right = right.next
        currentNode = currentNode.next
    right.next = None
    left.next = rightHead
    return leftHead

x = partitionLL(LL.head, 3)
while x:
    print(x.val)
    x = x.next
                


LL.showList()
        
        

        
    
