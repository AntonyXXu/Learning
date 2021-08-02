# https://leetcode.ca/all/159.html
import collections


def substr(s: str) -> int:
    if not s:
        return 0
    if len(s) <= 2:
        return len(s)

    strs = collections.Counter()
    longest = 0
    left = 0
    for right in range(len(s)):
        char = s[right]
        strs[char] += 1
        longest = max(longest, right - left)
        while len(strs) > 2:
            c = s[left]
            if strs[c] > 0:
                strs[c] -= 1
            if strs[c] == 0:
                del strs[c]
            left += 1
    return max(longest, len(s) - left)


print(substr("eceba"))
print(substr("ccaabbb"))
