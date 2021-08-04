# https://leetcode.com/problems/basic-calculator-ii/

def calc(s: str):
    if not s:
        return 0
    stk = []
    curr = 0
    op = '+'
    for i in range(len(s)):
        if s[i].isdigit():
            curr = curr * 10 + int(s[i])
        if s[i] in "+-*/" or i == len(s) - 1:
            if op == "+":
                stk.append(curr)
            elif op == "-":
                stk.append(-curr)
            elif op == "*":
                stk.append(stk.pop()*curr)
            else:
                stk.append(int(stk.pop()/curr))
            curr = 0
            op = s[i]

    return sum(stk)


print(calc(s="3+2*2"))
