# https://leetcode.com/problems/find-and-replace-pattern/

# Assuming pattern length is equal to word length in words

words = ["ccc","deq","mee","aqq","dkd","abc"]
p = "abb"
w1 = ["a","b","c"]
p1 = ["a"]

def pattern(words, pat):
    res = []
    d = {}
    p = []
    p.append(pat[0])
    p_index = 0
    d[pat[0]] = p_index
    for i in range(1,len(pat)):
        if pat[i] == pat[i-1]:
            p[p_index] += pat[i]   
        else:
            if pat[i] not in d.keys():
                d[pat[i]] = i
            p_index += 1
            p.append(pat[i])
    for word in words:
        same = True
        if len(word) != len(pat):
            break
        x = 0
        y = 0
        for i in range(0,len(word)):
            if y >= len(p[x]):
                x += 1
                y = 0
            if y != 0:
                if word[i] != word[i-1]:
                    same = False
                    break
            else:
                if i > 0 and word[i] == word[i-1]:
                    same = False
                    break
                if p[x][0] in d.keys():
                    index = d[p[x][y]]
                    if word[i] != word[index]:
                        same = False
                        break
            y += 1
        if same:
            res.append(word)
    return res

print(pattern(words, p))
print(pattern(w1, p1))
