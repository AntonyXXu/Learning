# https://leetcode.com/problems/letter-case-permutation/
import collections

def helper(prefix, index, s, ans):
    if len(prefix) == len(s):
        ans.append(prefix)
    else:
        if s[index].isalpha():
            helper(prefix + s[index].swapcase(), index + 1, s, ans)
        helper(prefix + s[index], index + 1, s, ans)
    return ans


def letterCase(s):
    ans = []
    a = helper('', 0, s, ans)
    return a

# BFS
def letterCase(s):
    if not s or len(s) == 0:
        return s
    dq = collections.deque(s)
    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            for i in range(len(s)):
                string = dq.popleft()
                left = string[:i]
                right = string[i+1:]

                dq.append(left + c + right)
                dq.append(left + c.swapcase() + right)
    return ''.join(list(dq))

print(letterCase(s = "a1b2"))
print(letterCase(s = "3z4"))
print(letterCase(s = "12345"))
print(letterCase(s = "0"))
print(letterCase(s = "abc"))
