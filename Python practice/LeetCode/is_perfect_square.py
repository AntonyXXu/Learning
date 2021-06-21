def sq(num):
    low = 0
    high = num

    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 == num:
            return True
        if mid ** 2 < num:
            low = mid + 1
        elif mid ** 2 > num:
            high = mid - 1
    return False

print(sq(1000))
print(sq(10000))