#Sort Stack:
from random import randint
class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    def push(self, val):
        self.arr.append(val)
        self.size += 1
    def peek(self):
        return self.arr[-1]
    def pop(self):
        self.size -= 1
        return self.arr.pop()
    
stk = Stack()

def sortStk(stk):
    tempStk = Stack()
    temp = 0
    while stk.size > 0:
        temp = stk.pop()
        while tempStk.size > 0 and temp < tempStk.peek():
            stk.push(tempStk.pop())
        tempStk.push(temp)
    while tempStk.size:
        stk.push(tempStk.pop())

for i in range(10):
    stk.push(randint(0,10))

sortStk(stk)

print(stk.arr)