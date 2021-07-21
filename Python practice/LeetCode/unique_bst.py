# https://leetcode.com/problems/unique-binary-search-trees/

def numTrees(n):
    if not n:
        return n
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[-1]
    
print(numTrees(3))
print(numTrees(1))