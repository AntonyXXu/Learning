# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

s = "abbc"
t = "aabb"
s1 = "leetcode"
t1 = "practice"
def minSteps(s, t):
    if len(s) != len(t):
        return -1
    chars = {}
    for letter in s:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    
    for letter in t:
        if letter in chars:
            chars[letter] -= 1
    
    total = 0
    for num in chars.values():
        if num > 0:
            total += num
    return total

print(minSteps(s,t))
print(minSteps(s1,t1))
print(minSteps("a","a"))