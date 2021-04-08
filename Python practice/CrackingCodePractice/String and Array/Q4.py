def pallindrome(str1):
    strArray = [0]*128
    for x in str1:
        arr_index = ord(x)
        strArray[arr_index] +=1
    print(strArray)
    odd = 0
    for i in strArray:
        if i % 2 == 1:
            odd += 1
    if odd > 1:
        return False
    return True

str1 = "aabbccdee"

print(pallindrome(str1))