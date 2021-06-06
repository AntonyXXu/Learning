# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

s = "())"
s1 = "((("
s2 = "()"
s3 = "()))(("

def valid(s):
    stk = []
    counter = 0
    for i in range(len(s)):
        if s[i] == "(":
            stk.append("(")
        else:
            if len(stk) == 0:
                counter += 1
            else: 
                stk.pop()
    return counter + len(stk)
    
print(valid(s))
print(valid(s1))
print(valid(s2))
print(valid(s3))