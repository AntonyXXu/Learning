# Given a sorted and rotated array, find if there is a pair with a given sum

# Input: arr[] = {11, 15, 6, 8, 9, 10}, x = 16
# Output: true
# There is a pair (6, 10) with sum 16

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
# Output: true
# There is a pair (26, 9) with sum 35

# Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 45
# Output: false
# There is no pair with sum 45.
x1 = [11, 15, 6, 7, 9, 10]
y1 = 16
x2 = [11, 15, 26, 38, 9, 10]
y2 = 35
y3 = 45

def hashing(arr, sumVal):
    nums = set()
    for i in range(len(arr)):
        otherV = sumVal - arr[i]
        if otherV in nums:
            return True
        else:
            nums.add(arr[i])
    return False
# print(hashing(x1, y1))

def hashingAll(arr, sumVal):
    nums = dict()
    ans = []
    for index, value in enumerate(arr):
        otherV = sumVal - arr[index]
        if otherV in nums:
            ans.append([nums[otherV], index])
        nums[value] = index
    return ans
# print(hashingAll(x1, y1))

def findPivotIt(arr):
    high = len(arr) - 1
    low = 0
    if high == low:
        return low
    while low < high:
        mid = (high + low) // 2
        if arr[mid - 1] > arr[mid]:
            return mid
        elif arr[mid] > arr[mid + 1]:
            return mid + 1
        else:
            if arr[mid] > arr[low]:
                low = mid + 1
            else:
                high = mid - 1
    return 0

def findSum(arr, sumVal):
    length = len(arr)
    if length <= 1:
        return False
    pivot = findPivotIt(arr)
    p1 = pivot
    p2 = pivot - 1 if pivot else length-1
    while p1 != p2:
        ptrSum = arr[p1] + arr[p2]
        if ptrSum == sumVal:
            return True
        elif ptrSum > sumVal:
            p2 = p2 - 1 if p2 else length-1
        else:
            p1 = (p1+1) % length
    return False

print(findSum([1,2,2],4))

def countSumAll(arr, sumVal):
    length = len(arr)
    ans = 0
    if length <= 1:
        return ans
    pivot = findPivotIt(arr)
    p1 = pivot
    p2 = pivot - 1 if pivot else length - 1
    while p1 != p2:
        ptrSum = arr[p1] + arr[p2]
        if ptrSum == sumVal:
            ans += 1
            p1 = (p1+1)%length
            continue
        elif ptrSum < sumVal:
            p1 = (p1+1)% length
        else:
            p2 = p2-1 if p2 else length-1
    return ans

print(countSumAll(x1,y1))