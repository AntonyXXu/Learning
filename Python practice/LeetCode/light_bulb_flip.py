# https://leetcode.com/problems/bulb-switcher-iv/

def flip(s):
    if len(s) == 0:
        return 0
    ans = 1 if s[0] == '1' else 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            ans += 1
    return ans

print(flip('1'))
print(flip('10111'))
print(flip('101'))
print(flip('000'))