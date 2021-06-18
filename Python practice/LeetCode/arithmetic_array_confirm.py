def arithmetic(arr):
    if len(arr) <= 1:
        return True
    arr.sort()
    diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True

a = [3,5,1]
b = [1,2,4]

print(arithmetic(a))
print(arithmetic(b))

def ar(arr):
    mini = arr[0]
    maxi = arr[0]
    for num in arr:
        mini = min(mini, num)
        maxi = max(maxi, num)
    interval = int((maxi - mini) / (len(arr)-1))
    if interval == 0:
        return True
    if interval % 1 != 0:
        return False
    for num in arr:
        diff = num - mini
        if diff % interval != 0:
            return False
    return True

print(ar(a))
print(ar(b))
