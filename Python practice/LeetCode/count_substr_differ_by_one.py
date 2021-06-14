# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

def countS(s1, s2):
    ans = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            index = 0
            diff = 0
            while i + index < len(s1) and j + index < len(s2) and diff < 2:
                if s1[i+index] != s2[j + index]:
                    diff += 1
                if diff == 1:
                    ans += 1
                index += 1
    return ans

print(countS('aba', 'baba'))
print(countS('ab', 'bb'))
print(countS('a', 'a'))
print(countS('abe', 'bbc'))