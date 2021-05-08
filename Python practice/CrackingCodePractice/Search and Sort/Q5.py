#Sparse String

x = ["", "at", "", "", "ball", "", "", "cop", "", "", "", "", "dad", "", ""]

def find(arr, string):
    i = 0
    j = len(arr)-1
    while i <= j:
        mid = (i + j) // 2
        
        if arr[mid] == "":
            left = mid - 1
            right = mid + 1
            while True:
                if left >= i and arr[left] == "":
                    left -= 1
                else:
                    mid = left
                    break
                if right <= j and arr[right] == "":
                    right += 1
                else:
                    mid = right
                    break
                if left < i and right > j:
                    return -1
        if mid < i or mid > j:
            return -1
        if arr[mid] == string:
            return mid
        if string < arr[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return -1

print(find (x, "cop"))
                