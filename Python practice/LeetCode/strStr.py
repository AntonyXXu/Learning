#Implement strStr()

# return first instance index

def strStr(s1, s2):
    if s1 == s2 or len(s2) == 0:
        return 0
    for i in range(len(s1)):
        eq = True
        for j in range(len(s2)):
            if s1[i+j] != s2[j]:
                eq = False
                break
        if eq:
            return i
    return -1

x = "hello"
y = "o"

print(strStr("",""))
print(strStr(x,y))