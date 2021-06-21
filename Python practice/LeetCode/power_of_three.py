def pwr(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 3 == 0:
        return pwr(n/3)
    else:
        return False