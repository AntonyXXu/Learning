# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def length(s):
    ans = 0
    first = 0
    chars = {}
    for i, letter in enumerate(s):
        if letter in chars and first <= chars[letter]:
            first = chars[letter] + 1
        ans = max(ans, i - first+1)
        chars[letter] = i

    return ans
        
print(length("abcabcbb"))
print(length("bbbbb"))
print(length("pwwkew"))
print(length("aab"))
print(length("dvdf"))