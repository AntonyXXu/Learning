# https://leetcode.com/problems/unique-paths/

def uniquePaths(m, n):
    if not m or not n:
        return 0
    current = [1] * n
    for row in range(1, m):
        for col in range(1, n):
            current[col] += current[col-1]
    return current[n-1]


print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(7, 3))
print(uniquePaths(3, 3))