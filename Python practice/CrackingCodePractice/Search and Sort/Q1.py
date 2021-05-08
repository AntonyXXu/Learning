lstA = [1,4,6,7,56]
lstB = [2,5,8,9,11,None,None,None,None,None]

# Assuming B is larger 
def merge(a, b, lasta, lastb):
    i = lasta
    j = lastb
    
    for index in range(len(b)-1, 0, -1):
        if (i >= 0 and a[i] > b[j]):
            b[index] = a[i]
            i-=1
        else:
            b[index] = b[j]
            j-=1

merge(lstA,lstB,4,4)
print(lstB)

