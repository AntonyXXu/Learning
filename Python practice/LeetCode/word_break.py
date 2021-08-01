# https://leetcode.com/problems/word-break/

def wordBreak(s, wordDict):
    st = set(wordDict)
    return dfs(s, st)


def dfs(s, st):
    if s in st:
        return True
    for i in range(1, len(s)+1):
        if s[:i] in st:
            res = dfs(s[i:], st)
            if res:
                return True
    return False


def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s)+1):
        for word in wordDict:
            if i - len(word) >= 0:
                prev = s[i - len(word):i]
                if word == prev and dp[i - len(word)] == True:
                    dp[i] = True
    return dp[-1]


print(wordBreak(s="leetcode", wordDict=["leet", "code"]))
print(wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
