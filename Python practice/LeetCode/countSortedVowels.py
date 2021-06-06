# https://leetcode.com/problems/count-sorted-vowel-strings/

def sortVowelString(n):
    res = [1] * 5
    for i in range(n):
        res[0] = res[0] + res[1] + res[2] + res[3] + res[4]
        res[1] = res[1] + res[2] + res[3] + res[4]
        res[2] = res[2] + res[3] + res[4]
        res[3] = res[3] + res[4]
        res[4] = res[4]

    return res[0]

print(sortVowelString(1))
print(sortVowelString(2))
print(sortVowelString(33))