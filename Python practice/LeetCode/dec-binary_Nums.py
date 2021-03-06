# A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. 
# For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

# Given a string n that represents a positive decimal integer, 
# return the minimum number of positive deci-binary numbers needed so that they sum up to n.

# Example 1:
# Input: n = "32"
# Output: 3
# Explanation: 10 + 11 + 11 = 32
# Example 2:
# Input: n = "82734"
# Output: 8
# Example 3:
# Input: n = "27346209830709182346"
# Output: 9

n1 = "32"
n2 = "82734"
n3 = "27346209830709182346"

def deciBinary(arr):
    max = 0
    for i in range(len(arr)):
        if max < int(arr[i]):
            max = int(arr[i])
    return max

def alternate(arr):
    nums = [1]*len(arr)
    lst = [int(i) for i in arr]
    counter = 0
    while True:
        changes = False
        for i in range(len(arr)):
            if lst[i] == 0:
                nums[i] = 0
            if lst[i] > 0:
                changes = True
            lst[i] -= nums[i]
        if not changes:
            return counter
        counter += 1


print(deciBinary(n1))
print(deciBinary(n3))
print(deciBinary(n2))


print(alternate(n1))
print(alternate(n3))
print(alternate(n2))