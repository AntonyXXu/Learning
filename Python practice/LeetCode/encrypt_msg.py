class Encrypt:
    def __init__(self, key):
        self.keys = {}
        self.createKeys(key)

    def createKeys(self, key: str):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_i = 0
        for letter in key:
            if letter.isalpha() and letter.lower() not in self.keys.values():
                self.keys[alpha[alpha_i]] = letter.lower()
                alpha_i += 1
        print(self.keys)

    def encrypt(self, phrase: str):
        res = []
        for letter in phrase:
            if letter.lower() in self.keys:
                appendLetter = self.keys[letter.lower()]
                if letter.isupper():
                    res.append(appendLetter.upper())
                else:
                    res.append(appendLetter.lower())
            else:
                res.append(letter)
        return ''.join(res)


def decrypt(d: str, c: str):
    if not c or c == '0' or not d:
        return []
    # find all uniques of c
    cipher = set()
    if len(c) == 1:
        cipher.add(1)
    else:
        prev1 = [c[0]]
        prev2 = [c[0]]
        for i in range(1, len(c)):
            curr = int(c[i-1:i+1])
            currentPermutes = []
            if curr % 10 == 0 and curr > 30:
                return []
            elif curr % 10 == 0:
                currentPermutes.append()
            elif curr > 10:
                set.add(curr//10)
            i += 1
    # map all unique letters in d
    di = {}
    for word in d:
        uniques = len(set(word))
        if uniques not in d:
            d[uniques] = []
        d[uniques].append(word)

    res = []
    for num in cipher:
        if num in di:
            res.extend(di[num])
    return res
