# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:01:59 2021

@author: Test
"""

#BST
class TreeNode():
    def __init__(self,key,value,left = None, right = None, parent = None):
        self.__key = key
        self.__value = value
        self.__left= left
        self.__right = right
        self.__parent = parent
        
    def getkey(self):
        return self.__key
    
    def getvalue(self):
        return self.__value
    
    def getleft(self):
        return self.__left
    
    def getright(self):
        return self.__right
    
    def getparent(self):
        return self.__parent
    
    def setkey(self,key):
        self.__key = key
        
    def setvalue(self,value):
        self.__value = value
    
    def setparent(self,parent):
        self.__parent = parent
        
    def setleft(self,left):
        self.__left = left
    
    def setright(self,right):
        self.__right = right
        
class BinarySearchTree():
    def __init__(self):
        self.__root = None
        self.__size = 0
        
    def getsize(self):
        return self.__size
    
    def getroot(self):
        return self.__root
    
    def get(self,key):
        return self.__get(key,self.__root)
    
    def __get(self,key,current):
        if current == None:
            return current
        elif key == current.getkey():
            return current.getvalue()
        elif key < current.getkey():
            return self.__get(key,current.getleft())
        elif key > current.getkey():
            return self.__get(key,current.getright())
        
    def insert(self,key,value):
        if self.__root == None:
            self.__root = TreeNode(key,value)
            self.__size = self.__size + 1
        else:
            self._add(key,value,self.__root)
    
    def _add(self,key,value,current):
        if current.getkey() == key:
            current.setvalue(value)
        elif key < current.getkey():
            if current.getleft() == None:
                current.setleft(TreeNode(key,value,parent = current))
                self.__size+=1
            else:
                self._add(key,value,current.getleft())
        else:
            if current.getright()==None:
                current.setright(TreeNode(key,value,parent = current))
                self.__size+=1
            else:
                self._add(key,value,current.getright())
                
    def delete(self,key):
        if self.__size == 1 and self.getroot() == key:
            self.__root = None
            self.__size -=1
        elif self.__size > 1:
            deleteNode = self._locate(key,self.__root)
            if deleteNode:
                self._remove(deleteNode)
                self.__size -=1
            else:
                raise KeyError("Key not in tree")
        else:
            raise KeyError("Key not in tree")
        
    def _locate(self,key,current):
        if not current:
            return None
        elif current.getkey() == key:
            return current
        elif current.getkey() < key:
            return self._locate(key,current.getright())
        else:
            return self._locate(key,current.getleft())
      
    def _remove(self,current):
        parent = current.getparent()
        left = current.getleft()
        right = current.getright()
        
        if left == None and right == None:
            if current == parent.getleft():
                parent.setleft(None)
            else:
                parent.setright(None)
        elif left == None and right:
            if parent == None:
                self.__root = right
            elif current == parent.getleft():
                parent.setleft(right)
            else:
                parent.setright(right)
            right.setparent(parent)
        elif right == None and left:
            if parent == None:
                self.__root = left
            elif current == parent.getleft():
                parent.setleft(left)
            elif current == parent.getright():
                parent.setright(left)
        else:
            newNode = self._findsmallest(current.getright())
            current.setkey(newNode.getkey())
            current.setvalue(newNode.getvalue())
            self._remove(newNode)
    
    def _findsmallest(self,currentNode):
        while currentNode.getleft():
            currentNode = currentNode.getleft()
        else:
            return currentNode
        
    def _inorder(self,node):
        if node != None:
            self._inorder(node.getleft())
            print(node.getkey(),node.getvalue())
            self._inorder(node.getright())
            
    def inorderSearch(self):
        self._inorder(self.__root)
        
    def preorderSearch(self):
        self._preorder(self.__root)
    
    def _preorder(self,node):
        if node:
            print(node.getkey(),node.getvalue())
            self._preorder(node.getleft())
            self._preorder(node.getright())
            
t = BinarySearchTree()
t.insert(5,"a")

t.insert(9,"b")
t.insert(11,"c")
t.insert(3,"d")
t.insert(1,"e")
t.insert(2,"f")
t.insert(4,"g")

t.insert(5,"A")
t.insert(3,"D")
print(t.getsize())
print(t.get(5),t.get(3),sep = ",")
t.inorderSearch()
print("preorder search")
t.preorderSearch()
print("remove ")
t.delete(5)
t.preorderSearch()
print(t.getroot().getkey())