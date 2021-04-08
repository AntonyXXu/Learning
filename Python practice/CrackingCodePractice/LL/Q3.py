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

    def delMidNode(self, node):
        nextNode = node.next
        currNode = node
        currNode.val = nextNode.val
        currNode.next = nextNode.next


LL = LinkedList()
for i in range(5):
    LL.insertfront(i)
#LL.insert("t",1)
LL.delMidNode(LL.head.next)


LL.showList()
        
        

        
    
