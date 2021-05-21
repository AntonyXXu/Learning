class MinHeap:
  
    def __init__(self, maxsize = 100):
        self.maxsize = maxsize
        self.heap = [0] * maxsize
        self.count = 0
    
    def insert(self, val):
        if self.count == self.maxsize:
            self.maxsize *= 2
            copy = self.heap
            self.heap = [0] * self.maxsize
            for i, val in enumerate(copy):
                self.heap[i] = val
        i = self.count
        self.heap[i] = val
        self.count += 1
        while i > 0 and self.heap[i] < self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def pop(self):
        if self.count == 0:
            return
        retVal = self.heap[0]
        i = 0
        self.heap[i] = self.heap[self.count-1]
        while (2*i+1 < self.count and 2*i+2 < self.count and
        (self.heap[i] > self.heap[2*i+1] or self.heap[i] > self.heap[2*i+2])):
            if self.heap[2*i+1] < self.heap[2*i+2] :
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i] 
                i = 2*i + 1
            else:
                self.heap[i], self.heap[2*i+2]= self.heap[2*i+2], self.heap[i] 
                i = 2*i + 2
        self.heap[self.count-1] = 0
        self.count -= 1
        return retVal
    
test = MinHeap(5)
test.insert(4)
test.insert(3)
test.insert(5)
test.insert(10)
test.insert(1)
test.insert(15)
print(test.heap)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.heap)
print(test.count)

class MaxHeap:
    def __init__(self, length = 10):
        self.length = 10
        self.arr = [None] * 10
        self.size = 0

    def insert(self, val):
        if self.size == self.length:
            temp = self.arr
            self.length *= 2
            self.arr = [None] * self.length
            for i, num in enumerate(temp):
                self.arr[i] = num
        self.arr[self.size] = val
        i = self.size      
        while i > 0 and self.arr[i] > self.arr[(i-1)//2]:
            self.arr[i], self.arr[(i-1)//2] = self.arr[(i-1)//2], self.arr[i]
            i = (i-1)//2
        self.size += 1

    def pop(self):
        retv = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1
        self.arr[self.size] = None
        i = 0
        while (2*i + 1 < self.size and 2*i + 2 < self.size
            and (self.arr[i] <self.arr[2*i + 1] or self.arr[2*i + 2])):
                if self.arr[2*i + 1] > self.arr[2*i + 2]:
                    self.arr[i], self.arr[2*i + 1] = self.arr[2*i + 1], self.arr[i]
                    i = 2*i + 1
                else:
                    self.arr[i], self.arr[2*i + 2] = self.arr[2*i + 2], self.arr[i]
                    i = 2*i + 2
        return retv    
        


test = MaxHeap(5)
test.insert(4)
test.insert(3)
test.insert(5)
test.insert(10)
test.insert(1)
test.insert(15)
print(test.arr)
print(test.pop())
print(test.pop())
print(test.pop())
print(test.arr)
print(test.size)