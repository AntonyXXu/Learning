#URLify

def URLify(testString, length):
    return testString.strip().replace(" ", "%20")
print(URLify("Mr John Smith ", 13))

#
def URLify2(testString, length):
    space = " "
    replacement = "%20"
    replaceString = []
    lastChar = 0
    numSpace = 0
    #Trim last few spaces
    for x in range(len(testString)-1, 0, -1):
        if testString[x] != space:
            lastChar = x
            break
    #lastChar is last character without space
    for x in range(0, lastChar):
        if testString[x] == space:
            numSpace+=1
    replaceString = [""]*(length + 2*numSpace)
    index = len(replaceString)-1
    while lastChar >= 0:
        if testString[lastChar] != space:
            replaceString[index] = testString[lastChar]
            index-=1
            lastChar-=1
            continue
        replaceString[index] = "0"
        replaceString[index-1] = "2"
        replaceString[index-2] = "%"
        index-=3
        lastChar-=1
    return "".join(replaceString)
print(URLify2("Mr John Smith ", 13))


