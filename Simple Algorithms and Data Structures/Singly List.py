# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:58:02 2021

@author: Test
"""
#%%
#singly list
class singlyNode():
    def __init__(self,data,nextdata):
        self.data = data
        self.next = nextdata
        
    def setnext(self,newnext):
        self.next=newnext
    
    def setdata(self,newdata):
        self.data=newdata
    
    def getdata(self):
        return self.data
    
    def getnext(self):
        return self.next
        
class singlyList():
    def __init__(self):
        self.size = 0
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def length(self):
        return self.size
    
    def __str__(self):
        string = "["
        current = self.head
        i=0
        while current != None:
            if i>0:
                string = string+","
            temp = current.getdata()
            if temp != None:
                string = string + str(temp)
                i+=1
            current = current.getnext()
        string = string + "]"
        print(string)
        return string
    
    def add(self,item):
        temp = singlyNode(item,self.head)
        self.head = temp
        self.size+=1
        
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
        if not found:
            index = -1
        return index
    
    def remove(self,item):
        current = self.head
        found = False
        previous = None
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        assert found, "item is not in list"
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
        self.size -=1
        
    def append(self,item):
        temp = singlyNode(item,None)
        if (self.head == None):
            self.head = temp
        else:
            current = self.head
            while (current.getnext() != None):
                current = current.getnext()
            current.setnext(temp)
        self.size+=1
        
    def pop(self):
        current = self.head
        previous = None
        while (current.getnext() != None):
            previous = current
            current = current.getnext()
        if previous == None:
            self.head = None
        else:
            previous.setnext(None)
        self.size -=1
        return current.getdata()
    
    def poppos(self,pos):
        current = self.head
        previous = None
        if pos == 0:
            self.head = current.getnext()
        else: 
            i = 0
            while i <= pos:
                i+=1
                previous = current
                current = current.getnext()
            previous.setnext(current.getnext())
        self.size -=1
        return current.getdata()
        
                
        
List = singlyList()
print(List.isEmpty())
List.add("a")
print(List.search("a"))
print(List.index("a"))
print(List.isEmpty())

print("add b")
List.add("b")
print(List.search("b"))
print(List.index("a"))

print("remove b")
List.remove("b")
print(List.search("b"))
print(List.index("b"))
List.add("b")
List.add("c")

print(List.length())

print("pop()")
print(List.pop())
print(List.index("a"))
print(List.length())

List.append("a")
print(List.index("a"))
print(List.length())

List.add("a")
List.append("f")

List.__str__()
print(List.poppos(1))
List.__str__()

