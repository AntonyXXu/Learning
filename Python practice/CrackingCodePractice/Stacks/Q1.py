#3 stacks in an array
class stkArray:
    def __init__(self, stackSize):
        self.arr = [0]*stackSize*3
        self.top = [0, stackSize, stackSize*2]
        self.size = [0]*3
        self.stackSize = stackSize

    def isEmpty(self, stackN):
        return self.size[stackN-1] == 0

    def isFull(self):
        return sum(self.size) == stackSize

    def push(self, val, stackN):
        if self.size[stackN-1] == self.stackSize:
            print("stk full")
            return -1
        self.arr[ self.top[stackN-1] ] = val
        self.top[stackN-1] += 1
        self.size[stackN - 1] += 1

    def peek(self, stackN):
        return self.arr[self.top[stackN-1]-1]

    def pop(self, stackN):
        if self.isEmpty(stackN):
            print("stack is empty")
            return None
        returnVal = self.peek(stackN)
        self.top[stackN - 1] -= 1
        self.size[stackN - 1] -= 1
        return returnVal
    #def pop:

    #def peek:



stk = stkArray(5)
stk.push(2,2)
stk.pop(2)
print(stk.pop(2))
print(stk.peek(2))
print(stk.arr)
print(stk.top)
for i in range(1,4):
    print(stk.isEmpty(i))

