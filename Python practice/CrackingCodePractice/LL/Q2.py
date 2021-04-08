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

    def getkToLast(self, k):
        if k > self.size-1 or k < 0:
            return -1
        kToFront = self.size - 1 - k
        currNode = self.head
        while kToFront >0:
            currNode = currNode.next
            kToFront-=1
        return currNode.val

    def getK(self, k):
        ptr1 = self.head
        ptr2 = self.head
        for i in range(k):
            ptr1 = ptr1.next
        while ptr1:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        return ptr2.val


LL = LinkedList()
for i in range(5):
    LL.insertfront(i)
#LL.insert("t",1)

x = LL.getK(1)

print(x)
LL.showList()
        
        

        
    
