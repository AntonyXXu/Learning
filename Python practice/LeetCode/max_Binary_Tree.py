# You are given an integer array nums with no duplicates. 
# A maximum binary tree can be built recursively from nums using the following algorithm:

# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.

nums = [3,2,1,6,0,5]
nums1 = [3,2,1]

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def maxBT(arr):
    maxI = 0
    for i in range(len(arr)):
        if arr[i] > arr[maxI]:
            maxI = i
    root = Node(arr[maxI])
    currNode = root
    currNode.left = branch(arr, 0, maxI - 1)
    currNode.right = branch(arr, maxI+1, len(arr)-1)
    return root

def branch(arr, low, high):
    if low < 0 or high > len(arr) - 1 or low > high:
        return None
    maxI = low
    for i in range(low, high+1):
        if arr[i] > arr[maxI]:
            maxI = i
    node = Node(arr[maxI])
    node.left = branch(arr, low, maxI - 1)
    node.right = branch(arr, maxI+1, high)
    return node

r1 = maxBT(nums)
print(r1.right.val)