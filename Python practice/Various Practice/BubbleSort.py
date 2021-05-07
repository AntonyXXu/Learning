#bubble sort:
arr = [-12, 11, 0, -5, 6, -7, 5, -3, -6]

# def bubble(arr):
#     if len(arr) <= 1:
#         return
#     for i in range(len(arr) - 1):
#         swap = 0
#         for j in range(len(arr)-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swap += 1
#         if swap == 0:
#             return

def bubble(arr):
    for i in range(len(arr)-1):
        swaps = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps = True
        if not swaps:
            return




bubble(arr)
print(arr)