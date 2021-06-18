nums = [4,2,5,7]
n1 = [888,505,627,846]

def sortParity(arr): 
    odd = []
    even = []
    for num in arr:
        if num % 2 == 0: 
            even.append(num)
        else:
            odd.append(num)
    for i in range(len(odd)):
        arr[2*i] = even[i]
        arr[2*i+1] = odd[i]
    return arr
    
print(sortParity(nums))

def inplace(arr):
    odd = 1
    even = 0
    while odd < len(arr) and even < len(arr):
        if arr[even] % 2 == 0:
            odd += 2
        elif arr[odd] % 2 == 1:
            odd += 2
        else:
            arr[odd], arr[even] = arr[even], arr[odd]
            odd += 2
            even += 2
    return arr

print(inplace(nums))
print(inplace(n1))
