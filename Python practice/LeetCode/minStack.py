class MinStack:
    def __init__(self):
        self._minStack = []
        self._stack = []
        self.size = 0
    
    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            top = self._stack.pop()
            if top == self._minStack[-1]:
                self._minStack.pop()
            return top

    def top(self):
        if self.size == 0:
            return
        else:
            return self._stack[-1]

    def getMin(self):
        if self.size == 0:
            return
        return self._minStack[-1]

    def push(self, val):
        self._stack.append(val)
        if len(self._minStack) == 0 or val <= self._minStack[-1]:
            self._minStack.append(val)
        self.size += 1
