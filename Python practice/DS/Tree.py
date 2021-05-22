class binaryTree():
    def __init__(self,element):
        self.key = element
        self.left = None
        self.right = None

    def getleft(self):
        return self.left
    
    def getright(self):
        return self.right
    
    def getself(self):
        return self.key
    
    def setself(self,val):
        self.key = val

    def setleft(self,val):
        if self.left == None:
            self.left = binaryTree(val)
        else:
            temp = binaryTree(val)
            temp.left = self.left
            self.left = temp
            
    def setright(self,val):
        if self.right == None:
            self.right = binaryTree(val)
        else:
            temp = binaryTree(val)
            temp.right = self.right
            self.right = temp
    
# Tree Traversal
def preorder(tree):
    if tree !=None:
        print(tree.getself())
        preorder(tree.getleft())
        preorder(tree.getright())
        
def inorder(tree):
    if tree != None:
        inorder(tree.getleft())
        print(tree.getself())
        inorder(tree.getright())
        
def postorder(tree):
    if tree != None:
        postorder(tree.getleft())
        postorder(tree.getright())
        print(tree.getself())
            
test = binaryTree(1)
test.setleft(2)
test.setright(3)

preorder(test)
inorder(test)
postorder(test)


