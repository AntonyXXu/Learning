
def minChips(arr):
    odd = 0
    even = 0
    for chip in arr:
        if chip % 2 == 0:
            odd += 1
        else:
            even += 1
    return min(odd, even)
    