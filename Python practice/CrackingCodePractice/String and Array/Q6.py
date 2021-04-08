def stringConcat(str1):
    concat = [""]*len(str1)
    consecutive = 0
    concatIndex = 0
    for i in range(len(str1)):
        consecutive +=1
        if i + 1 >= len(str1) or str1[i] != str1[i+1]:
            concat[concatIndex] = str1[i]
            concat[concatIndex+1] = str(consecutive)
            concatIndex+=2
            consecutive = 0

    return "".join(concat)

x = stringConcat("aabcccccaaa")

print(x)