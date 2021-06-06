import collections
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class FindElements:
    def __init__(self, root: Node):
        self.root = root
        self.elem = set()
        n = root
        n.val = 0
        self.elem.add(n.val)
        self._fix(n)

    def find(self,val):
        return val in self.elem
        deq = collections.deque()
        n = self.root
        deq.appendleft(n)
        while len(deq):
            curr = deq.pop()
            if curr.val == val:
                return True
            if curr.left:
                deq.appendleft(curr.left)
            if curr.right:
                deq.appendleft(curr.right)

    def _fix(self, node):
        if not node:
            return
        if node.left:
            node.left.val = node.val * 2 + 1
            self.elem.add(node.left.val)
            self._fix(node.left)
        if node.right:
            node.right.val = node.val * 2 + 2
            self.elem.add(node.right.val)
            self._fix(node.right)
        

r = Node(-1)
r.left = Node(-1)
r.right = Node(-1)
r.left.left = Node(-1)
r.left.right = Node(-1)

f = FindElements(r)
