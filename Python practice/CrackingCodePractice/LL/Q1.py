#LL implementation
class Node:
    def __init__(self, val, nextval = None):
        self.val = val
        self.next = nextval
    def getVal(self):
        return self.val
    def getNext(self):
        return self.next
    def setNext(self, newNext):
        self.next = newNext
    def setval(self, newVal):
        self.val = newVal

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def getSize(self):
        return self.size
    def showList(self):
        curr = self.head
        while curr:
            print(curr.getVal(), end = " ")
            curr = curr.getNext()
        
    def insertFront(self, val):
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1
    
    def insertAfter(self, val, index):
        if index > self.getSize() - 1 or index < 0:
            return -1
        currNode = self.head
        for i in range(0, index+1):
            if i == index:
                temp = Node(val, currNode.getNext())
                currNode.setNext(temp)
                self.size+=1
                return i
            currNode = currNode.getNext()
    
    def deleteFront(self):
        if self.size == 0:
            return False
        self.head = self.head.getNext()
        self.size-=1
        return True
    
    def delete(self, index):
        if index >= self.size:
            return False
        if index == 0:
            return self.deleteFront()
        currNode = self.head
        i = 0
        while i < index - 1 :
            currNode = currNode.getNext()
            i+=1
        delNode = currNode.getNext()
        currNode.setNext(delNode.getNext())
        self.size-=1
        return True

    def search(self, val):
        currNode = self.head
        i = 0
        found = False
        while not found and currNode:
            if currNode.getVal() == val:
                return i
            currNode = currNode.getNext()
            i+=1
        return -1
    
    def count(self, val):
        currNode = self.head
        count = 0
        while currNode:
            if currNode.getVal() == val:
                count+=1
            currNode = currNode.getNext()
        return count
    
    # def removeDup(self):
    #     uniqueVals = set()
    #     currNode = self.head
    #     prevNode = None
    #     while currNode:                
    #         if currNode.getVal() in uniqueVals:
    #             prevNode.setNext(currNode.getNext())
    #         else:
    #             uniqueVals.add(currNode.getVal())
    #             prevNode = currNode
    #         currNode = currNode.getNext()
    def removeDup(self):
        setDup = set()
        currNode = self.head
        prevNode = None
        while currNode:
            if currNode.val in setDup:
                prevNode.next = currNode.next
            else:
                setDup.add(currNode.val)
                prevNode = currNode
            currNode = currNode.next

    def removeDup2(self):
        ptr1 = self.head
        while ptr1:
            ptr2 = ptr1.next
            prevPtr = ptr1
            while ptr2:
                if ptr2.val == ptr1.val:
                    prevPtr.next = ptr2.next
                else:
                    prevPtr = ptr2
                ptr2 = ptr2.next
            ptr1 = ptr1.next

    # def removeDup2(self):
    #     ptr1 = self.head
    #     while ptr1:
    #         ptr2 = ptr1
    #         while ptr2.next:
    #             if ptr2.next.val == ptr1.val:
    #                 ptr2.next = ptr2.next.next
    #                 self.size-=1
    #             else:
    #                 ptr2 = ptr2.next
    #         ptr1 = ptr1.next
        
            

            



LL = LinkedList()
LL.insertFront("a")
LL.insertFront("b")
LL.insertFront("c")
LL.insertAfter("d", 0)
LL.insertAfter("d", 3)
LL.insertAfter("d", 1)
LL.insertAfter("a", 0)
#LL.deleteFront()
#LL.delete(3)
#print(LL.search("d"))
#print(LL.count("d"))
LL.removeDup2()
LL.showList()

    