# https://leetcode.com/problems/generate-parentheses/

def generateParenthesis(n):
    ans = []
    if n == 0:
        return ans
    l = n
    r = n
    prefix = ''
    dfs(l, r, ans, prefix)
    return ans

def dfs(l, r, ans, prefix):
    if l == 0 and r == 0:
        ans.append(prefix)
        return
    if l > r:
        return
    if l:
        dfs(l-1, r, ans, prefix + '(')
    if r:
        dfs(l, r-1, ans, prefix + ')')
        
print(generateParenthesis(3))
print(generateParenthesis(0))
print(generateParenthesis(1))