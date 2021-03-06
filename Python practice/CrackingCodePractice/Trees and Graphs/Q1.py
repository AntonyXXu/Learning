#graph traversal

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Queue: 
    def __init__(self):
        self.size = 0
        self.front = None
        self.tail = None
    def push(self, val):
        if self.size == 0:
            self.front = Node(val, None)
            self.tail = self.front
            
        else:
            temp = Node(val, None)
            self.tail.next = temp
            self.tail = self.tail.next
        self.size += 1
    def pop(self):
        returnVal = self.front
        self.front = self.front.next
        self.size-=1
        return returnVal

q = Queue()
q.push(1)
q.push(2)
while q.size!= 0:
    print(q.pop().val)

# Assuming graph is a directed graph
def searchRoute(graph, nodeStart, nodeEnd):
    bfs = Queue()
    bfs.push(nodeStart)
    st = set()
    st.add(nodeStart)
    while bfs.size:
        curr = bfs.pop()
        for next in graph[curr]:
            if next == nodeEnd:
                return True
            st.add(next)
            bfs.push(next)
    return False