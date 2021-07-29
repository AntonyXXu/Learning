# https://leetcode.com/problems/palindrome-partitioning/

def partition(s):
    ans = []
    prefix = []
    dfs(s, prefix, ans)
    return ans

def dfs(s, prefix, ans):
    if not s:
        ans.append(prefix)
    else:
        for i in range(1, len(s) + 1):
            if pal(s[:i]):
                dfs(s[i:], prefix + [s[:i]], ans)

def pal(s):
    return s == s

print(partition("aab"))
print(partition("a"))

a = "abc"
reversed(a)
print(a)
