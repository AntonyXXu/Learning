#stack implementation via queue
class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    def push(self, val):
        self.arr.append(val)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.arr.pop()
    def peek(self):
        return self.arr[-1]
    def isEmpty(self):
        return self.size == 0
    
#Always push to stack 1
#when pop, check stack 2 empty. if empty, pop all of stack 1 to stack 2
#pop stack 2

class QueueStack:
    def __init__(self):
        self.stk1 = Stack()
        self.stk2 = Stack()
    def push(self, val):
        self.stk1.push(val)
    def size(self):
        return self.stk1.size + self.stk2.size
    def _transferStacks(self):
        while self.stk1.size > 0:
            temp = self.stk1.pop()
            self.stk2.push(temp)
    def pop(self):
        if self.size() == 0:
            return None
        elif self.stk2.size == 0:
            self._transferStacks()
        return self.stk2.pop()
    def peek(self):
        if self.size() == 0:
            return None
        elif self.stk2.size == 0:
            self._transferStacks()
        return self.stk2.peek()

x = QueueStack()
for i in range(10):
    x.push(i)

for i in range(5):
    x.pop()

for i in range(10):
    x.push(i)

for i in range(15):
    x.pop()

print(x.size())
print(x.stk1.arr)
print(x.stk2.arr)