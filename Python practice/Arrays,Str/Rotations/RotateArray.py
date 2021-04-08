arr = []
for i in range(10):
    arr.append(i)

def rotate(arr, size, rot):
    rot = rot%(size)
    if rot == 0:
        return arr
    tempArr = arr[-rot:]+arr[0:size-rot]
    return tempArr

#space complexity of 1
def rotate2(arr, size, rot):
    rot = rot%size
    if rot == 0:
        return
    for i in range(rot):
        temp = arr[0]
        for i in range(size-1):
            arr[i] = arr[i+1]
        arr[size-1] = temp
rotate2(arr, 10, 3)
print(arr)