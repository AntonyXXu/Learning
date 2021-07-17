# https://leetcode.com/problems/simplify-path/

def simplify(path):
    stk = []
    splitData = path.split('/')
    print(splitData)
    for char in splitData:
        if char == '.' or not char:
            continue
        elif char == '..':
            if stk:
                stk.pop()
        else:
            stk.append(char)
    
    return '/' + '/'.join(stk)

print(simplify("/home/"))