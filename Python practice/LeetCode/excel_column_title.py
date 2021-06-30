def titleToNumber(columnTitle):
    ans = 0
    for letter in columnTitle:
        ans *= 26
        ans += ord(letter) - ord("A") + 1
    return ans
print(titleToNumber("A"))
print(titleToNumber("AB"))
print(titleToNumber("ZY"))
print(titleToNumber("FXSHRXW"))
