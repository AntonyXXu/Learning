
x=[False]*128

testString = "1b1defghijk"

def duplicateString(testString):
    for i in range(len(testString)):
        num = ord(testString[i])
        if x[num] == True:
            return False
        x[num] = True
    return True

print(duplicateString(testString))


        

        
        