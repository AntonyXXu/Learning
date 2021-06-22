def substr(s):
    doubled = s + s
    return doubled[1:-1].find(s) != -1

print(substr('abcabc'))
print(substr('abcabcc'))
print(substr('abcabcabc'))