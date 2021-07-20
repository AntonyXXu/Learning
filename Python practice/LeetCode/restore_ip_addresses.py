# https://leetcode.com/problems/restore-ip-addresses/

def restoreIpAddresses(s):
    ans = []
    prefix = []
    index = 0
    dfs(s, index, prefix, ans)
    return ans

def dfs(s, index, prefix, ans):
    if len(prefix) > 4:
        return 
    if len(prefix) == 4 and index == len(s):
        ans.append('.'.join(prefix))
        return 
    for i in range(index, min(index + 3, len(s))):
        if s[index] == '0' and i > index:
            continue
        if int(s[index: i + 1]) < 256:
            dfs(s, i + 1, prefix + [s[index:i+1]], ans)


        