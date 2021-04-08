#stack with min value

class Stack:
    def __init__(self):
        self.stk = []
        self.size = 0
        self.minStack = []

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        return self.stk[-1]

    def min(self):
        if self.isEmpty():
            return None
        return self.minStack[-1]

    def push(self, val):
        if not self.minStack or val <= self.min():
            self.minStack.append(val)
        self.stk.append(val)
        self.size += 1

    def pop(self):
        self.size -= 1
        if self.peek() == self.min():
            self.minStack.pop()
        return self.stk.pop()

stk = Stack()
print(stk.isEmpty())
print(stk.peek())
for i in range(5,1,-1):
    stk.push(i)
stk.push(5)
stk.push(1)
print(stk.pop())
print(stk.stk)

print(stk.minStack)