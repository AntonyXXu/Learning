# https://leetcode.com/problems/license-key-formatting/

def license(s, k):
    ans = ""
    ctr = k
    for i in range(len(s)-1, -1, -1):
        if ctr == 0:
            ctr = k
            ans += "-"
        if s[i] != "-":
            ans += s[i]
            ctr -= 1 

    return ans[::-1]


print(license("5F3Z-2e-9-w",4))
print(license(s = "2-5g-3-J", k = 2))