def mutateTheArray(n, a):
    if n == 1:
        return a
    arr = []
    for i in range(len(a)):
        curr = a[i]
        if i - 1 < 0:
            low = 0
        else:
            low = a[i-1]
        if i + 1 > n - 1:
            high = 0
        else:
            high = a[i+1]
        arr.append(low + curr + high)
    return arr
            
