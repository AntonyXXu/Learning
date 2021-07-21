# 4:23

#letter cipher -> two words, can you change one word to another by changing one letter at a time
#lower case alphabet, no spaces, no #s, no special chars
#non empty and same

# "abc" -> "bcd"
# "test" -> "lsst"
# "bacc" -> "cacb"

# n1 total different letters s1
# n2 s2

# n1 < n2:
#     return False

import collections

def change(s1, s2):
    if s1 == s2:
        return True
    d1 = collections.Counter()
    d2 = collections.Counter()
    d = {}
    for letter in s1:
        d1[letter] += 1
    for letter in s2:
        d2[letter] += 1
    if len(d1.keys()) < len(d2.keys()) or (len(d1.keys()) == 26 and len(d2.keys()) == 26):
        return False
    
    for i, letter in enumerate(s1):
        if letter == s2[i]:
            continue
        if s2[i] not in d1:
            d[letter] = s2[i]

    for i, letter in enumerate(s1):
        if letter not in d:
            d[letter] = s2[i]

    result = []
    for letter in s1:
        result.append(d[letter])
    return ''.join(result) == s2

def change(s1, s2):
    
    d = {}
    for i, letter in enumerate(s1):
        if letter not in d:
            d[letter] = s2[i]
        elif d[letter] == s2[letter]:
            return False
    if len(d) == 26:
        return False
    return True

print(change("antony", "ferrar"))