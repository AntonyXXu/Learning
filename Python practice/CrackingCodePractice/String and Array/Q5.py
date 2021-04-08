def stringChecker(str1, str2):
    diff = len(str1) - len(str2)
    if abs(diff) == 0:
        return checkReplace(str1, str2)
    if diff == 1:
        return checkInsert(str1, str2)
    if diff == -1:
        return checkInsert(str2, str1)
    return False

def checkReplace(str1, str2):
    diff = False
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            if diff:
                return False
            diff = True
    return True

def checkInsert(longerStr, shorterStr):
    diff = False
    index2 = 0
    index1 = 0
    while index1 < len(longerStr) and index2 < len(shorterStr):
        if longerStr[index1] != shorterStr[index2]:
            if diff:
                return False
            #decrement index 2 to count again
            index2-=1
            diff = True
        index2+=1
        index1+=1
    return True


print(stringChecker("abfx","abx"))


