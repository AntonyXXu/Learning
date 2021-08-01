def wordBreak(s, wordDict):
    dp = [[] for _ in range(len(s)+1)]
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if len(word) <= i:
                if word == s[i - len(word):i]:
                    if i - len(word) == 0:
                        dp[i].append(word)

                    elif len(dp[i - len(word)]) > 0:
                        for j in range(len(dp[i-len(word)])):
                            prev = dp[i-len(word)][j]
                            dp[i].append(prev + " " + word)
    print(dp)
    return dp[-1]


print(wordBreak(s="catsanddog", wordDict=[
      "cat", "cats", "and", "sand", "dog"]))

print(wordBreak(s="pineapplepenapple", wordDict=[
      "apple", "pen", "applepen", "pine", "pineapple"]))
print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
