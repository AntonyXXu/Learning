# https://leetcode.com/problems/decode-ways/

def numDecodings(s):
    if not s or len(s) == 0 or s[0] == "0":
        return 0

    prev1 = 1
    prev2 = 1
    ans = 1

    for i in range(1, len(s)):
        num = int(s[i-1:i+1])
        ans = 0
        if not num or (num >= 30 and num % 10 == 0):
            return ans
        if num % 10 != 0:
            ans += prev1
        if 10 <= num and num <= 26:
            ans += prev2
        prev2 = prev1
        prev1 = ans

    return ans

print(numDecodings(    "12"     ))
print(numDecodings(    "226"     ))
print(numDecodings(   "0"     ))
print(numDecodings(    "06"     ))
print(numDecodings(    "10"     ))