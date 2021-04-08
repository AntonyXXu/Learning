#selection Sort

arr = [-12, 11, 0, -5, 6, -7, 5, -3, -6]

# def selectionSort(arr):
#     n = len(arr)
#     for i in range(n):
#         small = i
#         for j in range(i, n):
#             if arr[small] > arr[j]:
#                 small = j
#         arr[i], arr[small] = arr[small], arr[i]
    
def selectionSort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i,len(arr)):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    

selectionSort(arr)
print(arr)