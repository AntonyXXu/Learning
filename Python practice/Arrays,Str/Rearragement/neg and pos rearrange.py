#Rearrange positive and negative numbers using inbuilt sort function
#must not use additional data structures

x = [12, 11, -13, -5, 6, -7, 5, -3, -6]
y = [-12, 11, 0, -5, 6, -7, 5, -3, -6]

# insertion sort:

def rearrange(arr):
    n = len(arr)
    if n <= 1:
        return 
    zeroIndex = 0
    for i in range(1, n):
        if arr[i] < 0:
            temp = arr[i]
            j = i
            while j >= zeroIndex + 1:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
            zeroIndex += 1

rearrange(x)
print(x)
        

    


