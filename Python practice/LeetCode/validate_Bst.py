# https://leetcode.com/problems/validate-binary-search-tree/
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validate(root):
    if not root:
        return True
    stk = []
    curr = root
    num = None
    while True:
        if curr:
            stk.append(curr)
            curr = curr.left

        elif stk:
            curr = stk.pop()
            if num is not None and num >= curr.val:
                return False
            num = curr.val

            curr = curr.right
        
        else:
            break
    return True

r = Node(0, None, Node(-1))
print(validate(r))