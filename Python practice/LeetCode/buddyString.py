#return true if you can swap two chars within a string, else return false

a = "ab"
b = "ba"
a1 = "ab"
b1 = "ab"
a2 = "aa"
b2 = "aa"
a3 = "abb"
b3 = "abc"

def buddyString(s1, s2):
    if len(s1) != len(s2):
        return False
    st = set()
    diff = 0
    ch = ""
    for i in range(len(s1)):
        st.add(s1[i])
        if s1[i] != s2[i]:
            if s1[i] != ch and ch != "":
                return False 
            ch = s2[i]
            diff += 1
            if diff > 2:
                return False
    if diff == 2:
        return True
    if diff == 0:
        if len(st) != len(s1):
            return True
    return False

print(buddyString(a,b))
print(buddyString(a1,b1))
print(buddyString(a2,b2))
print(buddyString(a3,b3))


