# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

def letterCombinations(digits: str):
    if not digits:
        return []
    d = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'] , '7': ['p','q','r','s'] , '8': ['t','u','v'] , '9': ['w','x','y','z']}
    ans = []
    i = 0
    prefix = []
    dp(digits, prefix, ans, i, d)
    return ans

def dp(digits, prefix, ans, i, d):
    # Base case
    if i == len(digits):
        ans.append(''.join(prefix))
        return
    curr = digits[i]
    for letter in d[curr]:
        dp(digits, prefix+[letter], ans, i+1, d)

print(letterCombinations('' ))
print(letterCombinations('2' ))
print(letterCombinations('23' )==["ad","ae","af","bd","be","bf","cd","ce","cf"])
