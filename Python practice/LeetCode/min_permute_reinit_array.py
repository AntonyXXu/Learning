def reinit(n):
    ref = [i for i in range(n)]
    prev = ref[:]
    perm = ref[:]
    def p(arr, prev):
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = prev[i//2]
            else:
                arr[i] = prev[n//2 + (i-1)//2]
        for i in range(len(arr)):
            prev[i] = perm[i]

    p(perm, prev)
    ctr = 1
    while perm != ref:
        p(perm, prev)
        ctr += 1
    return ctr

print(reinit(6))