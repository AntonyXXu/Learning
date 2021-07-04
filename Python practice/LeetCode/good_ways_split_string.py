# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

def numSplits(s):
    ans = 0
    left = set()
    right = set(s)
    for i in range(len(s)):
        left.add(s[i])
        if s[i] not in s[i+1:]:
            right.remove(s[i])
        if len(left) == len(right):
            ans += 1
    return ans

print(numSplits( "aacaba"))
print(numSplits("abcd"))
print(numSplits("aaaaa"))
print(numSplits( "acbadbaada"))
print(numSplits( "a"))
            


