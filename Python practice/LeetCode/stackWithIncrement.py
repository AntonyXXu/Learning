# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []

    def push(self, val):
        if len(self.stack) >= self.size:
            return
        self.stack.append(val)
    
    def pop(self):
        if len(self.stack):
            return self.stack.pop()

    def increment(self, index, val):
        counter = 0
        while counter < index and counter < len(self.stack):
            self.stack[counter] += val
            counter += 1

s = Stack(10)
for i in range(11):
    s.push(i)

print(s.stack)
print(s.pop())
s.increment(5,10)
print(s.stack)
s.increment(100,5)
print(s.stack)