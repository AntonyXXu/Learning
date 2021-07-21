# https://leetcode.com/problems/interleaving-string/
def isInterleave(s1, s2, s3):
    if not s1 and not s2 and not s3:
        return True
    if len(s1) + len(s2) != len(s3):
        return False

    m = len(s1)
    n = len(s2)
    prev = [True] * (n+1)
    for i in range(n+1):
        prev[i] = prev[i-1] and s2[i-1] == s2[i-1]

    for i in range(m+1):
        current = [prev[0] and s1[i-1] == s3[i-1]] * (n+1)
        
        for j in range(n+1):
            current[j] = (current[j-1] and s2[j-1] == s3[i+j-1]) or \
                (prev[j-1] and s1[i-1] == s3[i+j-1])
        prev = current[:]
    return prev[-1]
