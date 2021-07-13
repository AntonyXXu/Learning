# https://leetcode.com/problems/integer-to-roman/

def intToRoman(num):
    d = {1000: 'M', 900: 'CM', 500: 'D', 400:'CD', 100: 'C', 90:'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    ans = ''
    for index, char in d.items():
        ans += num // index * char
        num %= index
    return ans

print(intToRoman(3 ))
print(intToRoman( 4))
print(intToRoman( 9))
print(intToRoman( 58))
print(intToRoman( 1994))
