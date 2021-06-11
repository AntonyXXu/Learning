# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
s1 = "(()())"
s2 =  "()(())()"
def depths(par):
    level = 0
    res = []
    for ch in par:
        if ch == '(':
            if level % 2 == 0:
                res.append(0)
            else:
                res.append(1)
            level += 1

        else:
            level -= 1
            if level % 2 == 0:
                res.append(0)
            else:
                res.append(1)

    return res
print(depths(s1))
print(depths(s2))