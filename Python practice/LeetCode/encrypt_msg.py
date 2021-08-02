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


e = Encrypt(
    'The quick onyx goblin, Grabbing his sword jump over the 1st lazy dwarf')

print(e.encrypt('It was all a dream.'))
