# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def eval(tokens):
    a = '+'
    s = '-'
    m = '*'
    d = '/'
    ops = set([a, s, m, d])
    stk = []
    for i in range(len(tokens)):
        if tokens[i] in ops:
            right = int(stk.pop())
            left = int(stk.pop())
            if tokens[i] == a:
                stk.append(left + right)
            if tokens[i] == s:
                stk.append(left - right)
            if tokens[i] == m:
                stk.append(left * right)
            if tokens[i] == d:
                if (left > 0 and right > 0) or (left < 0 and right < 0):
                    stk.append(left // right)
                else:
                    res = abs(left) // abs(right)
                    stk.append(-res)
        else:
            stk.append(tokens[i])
    return stk[-1]


print(eval(["2", "1", "+", "3", "*"]))
print(eval(["4", "13", "5", "/", "+"]))
print(eval(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(eval(["4", "-2", "/", "2", "-3", "-", "-"]))
