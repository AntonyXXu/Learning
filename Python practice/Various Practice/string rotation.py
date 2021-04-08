def stringRotate(str1):
    for i in range(len(str1)):
        print(str1[i:] + str1[:i])

stringRotate("abcd")