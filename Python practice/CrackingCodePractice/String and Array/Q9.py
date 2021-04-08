#IsSubstring provided, or use find()

def isRotation(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 == length2 and length1 > 0:
        str1Ext = str1+str1
        return str1Ext.find(str2)
    return -1

x = isRotation("abcde", "cxeab")
print(x)
