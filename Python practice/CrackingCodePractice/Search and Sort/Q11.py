#Peaks and Valleys

arr = [5,3,1,2,3]
arr1 = [9,1,0,4,8,7]

def pv(arr):
    res = sorted(arr)
    for i in range(1,len(res),2):
        res[i], res[i-1] = res[i-1], res[i]
    return res

print(pv(arr))
print(pv(arr1))

def optimalpv(arr):
    res = arr[:]
    for i in range(1,len(arr)-1):
        





    return res

print(optimalpv(arr))
print(optimalpv(arr1))