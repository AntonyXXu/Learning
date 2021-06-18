s = ["H","a","n","n","a","h"]
s1 = ["h","e","l","l","o"]

def reverseString(s):
    n = len(s)
    mid = n // 2
    for i in range(mid):
        s[i], s[n-1-i] = s[n-1-i], s[i]
    print(s)

reverseString(s)
reverseString(s1)