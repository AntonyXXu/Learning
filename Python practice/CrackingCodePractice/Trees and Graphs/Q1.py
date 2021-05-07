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
    def push(val):
        if self.size == 0:
            self.front = Node(val, None)
            self.tail = self.front
        else:
            temp = Node(val, None)
            self.tail.next = temp
            self.tail = self.tail.next
    def pop():
        returnVal = self.head
        self.head = self.head.next
        return returnVal

def traverse():

        