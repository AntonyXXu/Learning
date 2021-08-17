# stack of plates - array of stack, with popIndex()

class SetOfStacks:
    def __init__(self, maxSize):
        self.arrStack = []
        self.maxSize = maxSize
        self.size = 0
        self.currIndex = -1

    def push(self, val):
        newAdd = [val]
        if not self.arrStack or len(self.arrStack[self.currIndex]) == self.maxSize:
            self.arrStack.append(newAdd)
            self.currIndex += 1
        else:
            self.arrStack[self.currIndex].append(val)
        self.size += 1

    def pop(self):
        if not self.arrStack:
            return None
        popVal = self.arrStack[self.currIndex].pop()
        self.size -= 1
        if not self.arrStack[self.currIndex]:
            del self.arrStack[-1]
            self.currIndex -= 1
        return popVal

    def popIndex(self, index):
        if not self.arrStack or index > self.currIndex:
            return None
        popVal = self.arrStack[index].pop()
        self.size -= 1
        if not self.arrStack[index]:
            del self.arrStack[index]
            self.currIndex -= 1
        return popVal


stk = SetOfStacks(3)

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(1)
stk.popIndex(1)
stk.popIndex(1)
stk.popIndex(1)


print(stk.currIndex)
print(stk.arrStack)
print(stk.size)
