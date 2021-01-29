# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:32:03 2021

@author: Test
"""

#%%Queue
class Queue():
    def __init__(self):
        self.items=[]
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
        
    def isEmpty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
        
    def __str__(self):
        return str(self.items)

#Test
q = Queue()
q.show()
print(q.isEmpty())
q.enqueue("a")
q.show()
print(q.isEmpty())
q.enqueue("b")
q.enqueue("c")
q.show()
print(q.size())
deq = q.dequeue()
print(deq)
q.show()
print(q.size())

#%% Bounded Queue
class BQueue():
    def __init__(self,max):
        assert max >=0, "capacity must be greater than or equal to 0"
        self.__items=[]
        self.__max=max
        
    def enqueue(self,item):
        if len(self.__items)>=self.__max:
            raise Exception ("Error - Queue is full")
        else:
            self.__items.append(item)
    
    def dequeue(self):
        if len(self.__items)<=0:
            raise Exception ("Error - Queue is empty")
        return self.__items.pop(0)
    
    def peek(self):
        if len(self.__items)<=0:
            raise Exception ("Error - Queue is empty")
        return self.__items[0]
    
    def isEmpty(self):
        return self.__items==[]
    
    def isFull(self):
        return len(self.__items)==self.__max
    
    def size(self):
        return len(self.__items)
    
    def capacity(self):
        return self.__max
    
    def clear(self):
        self.__items=[]
    
    def __str__(self):
        string=""
        for i in self.__items:
            string+=str(self.__items[i])
        return string
    
    def show(self):
        print(self.__items)
    
b = BQueue(4)
b.show()
print(b.capacity())
for i in range(4):
    b.enqueue(i)
b.show()
b.isFull()
string = b.__str__()

#%% Circular Queue
class CQueue():
    def __init__(self,capacity):
        if type(capacity)!=int or capacity<=0:
            raise Exception ("capacity error")
        self.__items=[]
        self.__capacity=capacity
        self.__head=0
        self.__count=0
        self.__tail=0
        
    def enqueue(self,item):
        if self.__count >= self.__capacity:
            raise Exception ("Circular Queue at capacity")
        if self.__count<self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail]=item
        self.__count+=1
        self.__tail=(self.__tail+1)%self.__capacity
    
    def dequeue(self):
        if self.__count <= 0:
            raise Exception ("Circular Queue is empty")
        deq = self.__items[self.__head]
        self.__items[self.__head]=None
        self.__count-=1
        self.__head = (self.__head+1)%self.__capacity
        return deq
    
    def peek(self):
        if self.__count <= 0:
            raise Exception ("Circular Queue is empty")
        return self.__items[self.__head]
    
    def isEmpty(self):
        return self.__count == 0
        
    def isFull(self):
        return self.__count == self.__capacity
    
    def size(self):
        return self.__count
    
    def capacity(self):
        return self.__capacity
    
    def clear(self):
        self.__items = []
        self.__head = 0
        self.__count = 0
        self.__tail = 0
        
    def __str__(self):
        string = ""
        x = self.__head
        for i in range(self.__count):
            string += str(self.__items[x])
            x=(x+1)%self.__capacity
        return string
    
    def __repr__(self):
        return str(self.__items) + "\nH = " + str(self.__head) + "\nT = " + \
            str(self.__tail)+"\n("+str(self.__count)+"/"+str(self.__capacity)+")"
            
c=CQueue(4)
c.enqueue("a")
c.enqueue("b")
print(c.__repr__())
c.enqueue("C")
c.enqueue("d")
print(c.__str__())
print(c.__repr__())
c.dequeue()
print(c.__repr__())