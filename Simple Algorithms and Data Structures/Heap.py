class minHeap:
    def __init__(self, maxsize = 100):
        self.maxsize = maxsize
        self.heap = [0] * maxsize
        self.count = 0
    
    def leaf(self, index):
        return index >= self.count//2 and index <= self.count
    
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
        while val < self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

