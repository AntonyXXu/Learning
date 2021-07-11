# https://leetcode.com/problems/longest-palindromic-substring/
import collections
def longestPalindrome(s):
    ans = ''
    for i in range(len(s)):
        res_odd = helper(s, i, i)
        res_even = helper(s, i, i+1)
        ans = max(ans, res_odd, res_even, key=len)
    return ans

def helper(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]


# print(longestPalindrome("babad"))
# print(longestPalindrome("cbbd"))
# print(longestPalindrome("a"))
print(longestPalindrome("aa"))