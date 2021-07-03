# https://leetcode.com/problems/letter-case-permutation/

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

print(letterCase(s = "a1b2"))
print(letterCase(s = "3z4"))
print(letterCase(s = "12345"))
print(letterCase(s = "0"))
print(letterCase(s = "abc"))
