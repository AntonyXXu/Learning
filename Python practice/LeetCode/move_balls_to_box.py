# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. 
# Note that after doing so, there may be more than one ball in some boxes.

# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

# Each answer[i] is calculated considering the initial state of the boxes.

 

# Example 1:

# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, 
# and move one ball from the second box to the third box in one operation.

boxes = "110"
boxes1 = "001011"

#brute force
def minOps(boxes):
    res = [0] * len(boxes)
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if boxes[j] == "1":
                res[i] += abs(i - j)
    return res

print(minOps(boxes))
print(minOps(boxes1))


def minOps2(boxes):
    res = [0] * len(boxes)
    prev = 0
    ones = 0
    for i in range(len(boxes)):
        res[i] += prev
        if boxes[i] == "1":
            ones += 1
        prev += ones
    prev = 0
    ones = 0
    for j in range(len(boxes)-1, -1, -1):
        res[j] += prev
        if boxes[j] == "1":
            ones += 1
        prev += ones
    return res

print(minOps2(boxes))
print(minOps2(boxes1))