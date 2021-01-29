# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:55:57 2021

@author: Test
"""
#%% stack at beginning
#Singly List for stack
class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def isempty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def show(self):
        print(self.items)
        return self.items
    def __str__(self):
        return str(self.items)

#test

s=Stack()
s.show
print(s.isempty())
s.push("a")
print(s.isempty())
s.show()
s.push("b")
s.push("c")
s.show()
print(s.size())
item= s.peek()
popd=s.pop()
s.show()
print(s.size())

#Parenthesis Matcher
  
def check(string):
    checker=Stack()
    bal = True
    index = 0
    opener = "([{"
    closer = ")]}"
    while index < len(string) and bal:
        symbol = string[index]
        if symbol in opener:
            checker.push(symbol)
        else:
            if checker.isempty()==True:
                bal = False
            else: 
                top=checker.pop()
                if opener.index(top)==closer.index(symbol):
                    bal = True
                else:
                    bal = True
        index=index + 1
        
    if bal and checker.isempty():
        return True
    else:
        return False

print(check("()"))

print(check("([])[){[)})"))



#%% stack at end
class Stack2():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def isempty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    def show(self):
        print(self.items)

#test
s=Stack2()
s.show()
print (s.isempty())
s.push("bob")
s.show()
print (s.isempty())
s.push("eva")
s.push("paul")
s.show()
print (s.size())
item=s.peek()
print (item, "is on top of",s)
item=s.pop()
s.show()
print (item,"was on the stack")
print (s.size())