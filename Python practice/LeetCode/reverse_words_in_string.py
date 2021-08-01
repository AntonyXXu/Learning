# https://leetcode.com/problems/reverse-words-in-a-string/

def rev(s: str):
    words = []
    i = 0
    while i < len(s):
        prefix = []
        while i < len(s) and s[i] == ' ':
            i += 1
        while i < len(s) and s[i] != ' ':
            prefix.append(s[i])
            i += 1
        if prefix:
            words.append(prefix)
    words.reverse()
    res = []
    for i in range(len(words)):
        if i != 0:
            res.append(' ')
        for j in range(len(words[i])):
            res.append(words[i][j])
    return ''.join(res)


print(rev(s="a good   example"))
print(rev(s="the sky is blue"))
print(rev(s="  hello world  "))
print(rev(s="  Bob    Loves  Alice   "))
