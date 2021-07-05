# https://leetcode.com/problems/remove-duplicate-letters/
 
import collections


def removeDup(s):
    letters = {}
    for i in range(len(s)):
        letters[s[i]] = i
    res = []
    for i in range(len(s)):
        if s[i] not in res:
            if res:
                topLetter = res[-1]
                while res and s[i] < topLetter and i < letters[topLetter]:
                    res.pop()
            res.append(s[i])
    return ''.join(res)

    

print( removeDup("bcabc"))
print( removeDup("cbacdcbc"))

    
