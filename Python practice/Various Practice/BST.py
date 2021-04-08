class Node:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
    
class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
            self.size+=1
            return
        curr = self.root
        while True:
            if curr.val == val:
                return
            elif val < curr.val:
                if not curr.left:
                    curr.left = Node(val, parent = curr)
                    self.size+=1
                    return
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = Node(val, parent= curr)
                    self.size+=1
                    return
                else:
                    curr = curr.right

    def search(self, val):
        curr = self.root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def rec_search(self,val):
        return self._rec_search(val, self.root)

    def _rec_search(self, val, currNode):
        if not currNode:
            return None
        if currNode.val == val:
            return currNode
        elif val < currNode.val:
            return self._rec_search(val, currNode.left)
        else: #val > currNode.val
            return self._rec_search(val, currNode.right)
    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self, currNode):
        if not currNode:
            return
        print(currNode.val)
        self._preorder(currNode.left)
        self._preorder(currNode.right)
    
    def delete(self, val):
        if self.size < 1:
            return False
        elif self.size == 1:
            self.root = None
            self.size -= 1
            return True
        else:
            delNode = self.search(val)
            if delNode:
                self._delete_helper(val, delNode)
                self.size -= 1
                return True
            else:
                return False    
        
    def _delete_helper(self, val, curr):
        parent = curr.parent
        left = curr.left
        right = curr.right
        if not left and not right:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        elif not left and right:
            if not parent:
                self.root = right
            else:    
                if parent.left == curr:
                    parent.left = right
                else:
                    parent.right = right
            right.parent = parent            
        elif not right and left:
            if not parent:
                self.root = left
            else:
                if parent.left == curr:
                    parent.left = left
                else:
                    parent.right = left
            left.parent = parent
        else:
            replacement = self._find_largest(curr.left)
            curr.val = replacement.val
            self._delete_helper(val, replacement)
                
    def _find_smallest(self, node):
        while node.left:
            node = node.left
        return node
    def _find_largest(self, node):
        while node.right:
            node = node.right
        return node
                    
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(15)
bst.insert(30)
bst.insert(3)
bst.insert(8)
print(bst.search(8).val)
print(bst.delete(10))
bst.preorder()



        
