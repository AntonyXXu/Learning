class Node:
    def __init__(self, val, nextN = None):
        self.val = val
        self.next = nextN

class Deque:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = self.head
    
    def enQ(self, val):
        if not self.size:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = Node(val, None)
            self.tail.next = temp
            self.tail = temp
        self.size+=1

    def enQLeft(self, val):
        if not self.size:
            self.head = Node(val)
            self.tail = self.head
        else:
            temp = Node(val, self.head)
            self.head = temp
        self.size+=1

    def __str__(self):
        ptr = self.head
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        return str(arr)
        
    def deQ(self):
        if not self.size:
            return None
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp


dq = Deque()

for i in range(3):
    dq.enQ(i)

for i in range(10, 20, 3):
    dq.enQLeft(i)

while dq.size:
    print(dq.deQ().val)
    print(dq)

print(dq)