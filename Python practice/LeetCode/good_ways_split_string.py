# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

import collections


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


def numSplits(s):
    ans = 0
    left = collections.Counter()
    right = collections.Counter()
    for letter in s:
        right[letter] += 1

    for letter in s:
        left[letter] += 1
        right[letter] -= 1
        if right[letter] == 0:
            del right[letter]
        if len(left) == len(right):
            ans += 1
    return ans


print(numSplits("aacaba"))
print(numSplits("abcd"))
print(numSplits("aaaaa"))
print(numSplits("acbadbaada"))
print(numSplits("a"))
