# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

s = "xyzzaz"

s2 = "aababcabc"
s3 = "abc"

def count(s):
    if len(s) < 3:
        return 0
    ans = 0
    for i in range(2, len(s)):
        st = set([s[i], s[i-1],s[i-2]])
        if len(st) == 3:
            ans += 1
    return ans
    

print(count(s))
print(count(s2))
print(count(s3))
