# https://leetcode.com/problems/interleaving-string/
import collections


def isInterleave(s1, s2, s3):
    if not s1 and not s2 and not s3:
        return True
    if len(s1) + len(s2) != len(s3):
        return False

    m = len(s1)
    n = len(s2)
    prev = [True] * (n+1)
    for i in range(n+1):
        prev[i] = prev[i-1] and s2[i-1] == s3[i-1]

    for i in range(m+1):
        current = [prev[0] and s1[i-1] == s3[i-1]] * (n+1)

        for j in range(n+1):
            current[j] = (current[j-1] and s2[j-1] == s3[i+j-1]) or \
                (prev[j-1] and s1[i-1] == s3[i+j-1])
        prev = current[:]
    return prev[-1]


def bfs(s1, s2, s3):
    if not s1 or not s2 or not s3:
        return False
    a = len(s1)
    b = len(s2)
    z = len(s3)
    if a + b != z:
        return False
    q = collections.deque()
    visited = set()
    start = (0, 0)
    q.append(start)
    visited.add(start)
    while q:
        r, c = q.popleft()
        if r == a and c == b:
            return True
        if r+1 <= a and (r+1, c) not in visited and s1[r] == s3[r+c]:
            coord = (r+1, c)
            visited.add(coord)
            q.append(coord)
        if c+1 <= b and (r, c+1) not in visited and s2[c] == s3[r+c]:
            coord = (r, c+1)
            visited.add(coord)
            q.append(coord)
    return False


def interleave(s1, s2, s3):
    if not s1 or not s2 or not s3:
        return False
    a = len(s1)
    b = len(s2)
    c = len(s3)
    if a + b != c:
        return False

    arr = [[True for _ in range(b+1)] for _ in range(a+1)]

    for i in range(a+1):
        arr[i][0] = arr[i-1][0] and s1[i-1][0] == s3[i-1]
    for i in range(b+1):
        arr[0][i] = arr[0][i-1] and s2[0][i-1] == s3[i-1]
    for i in range(1, a+1):
        for j in range(1, b+1):
            arr[i][j] = (arr[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                (arr[i][j-1] and s2[j-1] == s3[i+j-1])
    return arr[-1][-1]


print(interleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(interleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
