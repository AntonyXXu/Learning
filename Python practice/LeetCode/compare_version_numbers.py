# https://leetcode.com/problems/compare-version-numbers/

def compare(version1: str, version2: str):
    v1 = version1.split('.')
    v2 = version2.split('.')
    i = 0
    j = 0
    while i < len(v1) and j < len(v2):
        if int(v1[i]) == int(v2[i]):
            i += 1
            j += 1
            continue
        elif int(v1[i]) < int(v2[i]):
            return -1
        else:
            return 1
    while i < len(v1):
        if int(v1[i]) > 0:
            return 1
        else:
            i += 1
    while j < len(v2):
        if int(v2[j]) > 0:
            return -1
        else:
            j += 1
    return 0


print(compare(version1="1.01", version2="1.001"))
print(compare(version1="1.0.1", version2="1"))
print(compare(version1="1.0", version2="1.0.0"))
print(compare(version1="0.1", version2="1.1"))
print(compare(version1="7.5.2.4", version2="7.5.3"))
