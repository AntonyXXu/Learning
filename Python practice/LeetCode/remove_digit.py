def removeOneDigit(s, t):
    ans = 0
    for index, letter in enumerate(s):
        if letter.isdigit():
            if s[:index] + s[index + 1:] < t:
                ans += 1
    for index, letter in enumerate(t):
        if letter.isdigit():
            if s < t[:index] + t[index + 1:]:
                ans += 1
    return ans