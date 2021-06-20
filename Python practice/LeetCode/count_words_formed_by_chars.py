words = ["cat","bt","hat","tree"]
chars = "atach"

words1 = ["hello","world","leetcode"]
chars1 = "welldonehoneyr"

def word(words, chars):
    c = {}
    for letter in chars:
        if letter not in c:
            c[letter] = 1
        else:
            c[letter] += 1
    ans = 0
    for word in words:
        cpy = c.copy()
        addVal = True
        for let in word:
            if let not in cpy:
                addVal = False
                break
            cpy[let] -= 1
            if cpy[let] < 0:
                addVal = False
                break
        if addVal:
            ans += len(word)
    return ans

print(word(words, chars))
print(word(words1, chars1))
