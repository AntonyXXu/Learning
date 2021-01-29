# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:35:00 2021

@author: Test
"""

#Doubly List
class DNode():
    def __init__(self,data,nextdata,prevdata):
        self.data = data
        self.prev = prevdata
        self.next = nextdata

    def setnext(self,nextdata):
        self.next = nextdata
    
    def getnext(self):
        return self.next
    
    def getdata(self):
        return self.data
    
    def setdata(self,data):
        self.data = data
        
    def setprev(self,prevdata):
        self.prev = prevdata
        
    def getprev(self):
        return self.prev
    
class DList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.size == 0
        
    def length(self):
        return self.size
    
    def __str__(self):
        current = self.head
        string = "["
        while current != None:
            temp = current.getdata()
            string = string + str(temp)
            current = current.getnext()
        string = string + "]"
        print(string)
        return string
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found
    
    def index(self,item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else: 
                current = current.getnext()
                index+=1
        if found:
            return index
        else:
            return -1
    
    def add(self,item):
        temp = DNode(item,self.head,None)
        if self.head != None:
            self.head.setprev(temp)
        else: 
            self.tail = temp
        self.head = temp
        self.size+=1
    
    def remove (self,item):
        current = self.head
        found = False
        previous = None
        while current.getdata() != None and not found:
            if current.getdata()==item:
                found = True
            else:
                previous = current
                current = current.getnext()
        assert found, "item does not exist"
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
        if current.getnext() == None:
            self.tail = previous
        else:
            current.getnext().setprev(previous)
        self.size-=1
    
    def append (self,item):
        temp = DNode(item,None,None)
        if self.head == None:
            self.head = temp
        else:
            self.tail.setnext(temp)
            temp.setprev(self.tail)
        self.tail = temp
        self.size+=1
    
    def pop(self):
        current = self.tail
        previous = self.tail.getprev()
        if self.size == 1:
            self.tail = None
            self.head = None
        previous.setnext(None)
        self.tail = previous
        self.size -=1
        return current.getdata()
    
    def insert(self,item,pos):
        assert pos <= self.size,"position is larger than size"    
        if pos == self.size:
            self.append(item)
            return
        elif pos == 0:
            self.add(item)
            return
        else:
            current = self.head
            previous = None
            for i in range(pos):
                previous = current
                current = current.getnext()
            temp = DNode(item,None,None)
            previous.setnext(temp)
            current.setprev(temp)
            temp.setprev(previous)
            temp.setnext(current)
            self.size+=1
               
    
d = DList()
a = DNode("b","c",None)
b = DNode("c",None,"b")
d.head = a
d.head.setnext(a)
a.setnext(b)
print(a.getdata())
print(b.getdata())
d.__str__()
print(d.search("c"))
print(d.index("a"))
print(d.index("c"))
d.add("a")
print(d.index('a'))
print(d.head.getdata())
d.__str__()
d.remove("c")
d.__str__()
d.append("c")
d.__str__()

x = DList()
x.add("a")
x.append("c")
x.append("b")
x.append("d")
x.add(123)
x.__str__()
print(x.pop())
x.__str__()
print(x.length())

x.insert("x",4)
x.__str__()
print(x.length())