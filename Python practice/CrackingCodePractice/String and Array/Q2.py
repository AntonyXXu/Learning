str1 = "abda"
str2 = "dBaa"

def permute1(str1, str2):
    if len(str1) != len(str2):
        return False
    x1 = "".join(sorted(str1.lower()))
    x2 = "".join(sorted(str2.lower()))
    return x1 == x2

def permute2(str1, str2):
    if len(str1) != len(str2):
        return False
    strArray = [0]*128
    for char in str1:
        strArray[ord(char.lower())]+=1
    for char in str2:
        strArray[ord(char.lower())]-=1
        if strArray[ord(char.lower())] < 0:
            return False
    return True


x = permute2(str1, str2)
print(x)