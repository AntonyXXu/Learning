# https://leetcode.ca/all/161.html

def oneEdit(s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
        return False

    if len(s) == len(t):
        return checkReplace(s, t)
    if len(s) > len(t):
        return checkInsert(s, t)
    else:
        return checkInsert(t, s)


def checkReplace(s, t):
    diff = False
    for i in range(len(s)):
        if s[i] != t[i]:
            if diff:
                return False
            diff = True
    return True


def checkInsert(s, t):
    j = 0
    diff = False
    for i in range(len(s)):
        if s[i] != t[j]:
            if diff:
                return False
            diff = True
        else:
            j += 1
    return True


print(oneEdit(s="ab", t="acb"))
print(oneEdit(s="cab", t="ad"))
print(oneEdit(s="1203", t="1213"))
