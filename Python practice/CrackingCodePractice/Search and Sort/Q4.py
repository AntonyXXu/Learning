# Sorted Search, no size
# data only supports positive integers

def findLast(listy, val):
    index = 1
    while listy.elementAt(index) != -1 and val > listy.elementAt(index):
        index *= 2
    return index

def search(listy, val):
    i = 0
    j = findLast(listy)
    while i <= j:
        mid = (i + j) // 2
        if val == listy.elementAt(mid):
            return mid
        if listy.elementAt(mid) == -1 or val < listy.elementAt(mid):
            j = mid -1
        else:
            i = mid + 1
    return -1
    
        
    
    
