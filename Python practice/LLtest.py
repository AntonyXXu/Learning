from random import randint
#linked list:
class Node:
    def __init__(self, val, nextv = None):
        self.val = val
        self.next = nextv

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, val):
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
        else:
            new = Node(val)
            self.tail.next = new
            self.tail = self.tail.next
        self.size += 1

    def show(self):
        curr = self.head
        while curr:
            print(curr.val, end = " ")
            curr = curr.next
    
    def getmid(self, node):
        slow = node
        fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergesort(self):
        first = self.head
        return self._mergesort(first)


    def _mergesort(self, first):
        if not first or not first.next:
            return first
        midNode = self.getmid(first)
        midNext = midNode.next
        midNode.next = None
        left = self._mergesort(first)
        right = self._mergesort(midNext)
        return self.merge(left, right)

    def merge(self, left, right):
        ptr1 = left
        ptr2 = right
        result = Node(None)
        resultH = result
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                result.next = Node(ptr1.val)
                result = result.next
                ptr1 = ptr1.next
            else:
                result.next = Node(ptr2.val)
                result = result.next
                ptr2 = ptr2.next
        while ptr1:
            result.next = Node(ptr1.val)
            result = result.next
            ptr1 = ptr1.next
        while ptr2:
            result.next = Node(ptr2.val)
            result = result.next
            ptr2 = ptr2.next
        return resultH.next
        

x = LL()
for i in range(8):
    x.insert(randint(10,30))
x.show()
print("")
y = x.mergesort()
while y:
    print(y.val, end = " ")
    y = y.next