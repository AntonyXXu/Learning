# https: // leetcode.com/problems/design-add-and-search-words-data-structure/
class TrieNode:
    def __init__(self, letter=None, end=False):
        self.children = {}
        self.letter = letter
        self.end = end


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        index = 0
        return self._searchHelper(curr, word, index)

    def _searchHelper(self, node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            return node.end
        if word[index] == '.':
            for letter in self.alphabet:
                if letter in node.children:
                    if self._searchHelper(node.children[letter], word, index + 1):
                        return True
            return False
        else:
            if word[index] in node.children:
                return self._searchHelper(node.children[word[index]], word, index + 1)
            else:
                return False


w = WordDictionary()
# w.addWord('bad')
# w.addWord('mad')
# w.addWord('dad')
# print(w.search('pad'))
# print(w.search('bad'))
# print(w.search('.ad'))
# print(w.search('b..'))
w.addWord('a')
w.addWord('ab')
print(w.search('a'))
print(w.search('a.'))
print(w.search('ab'))
print(w.search('.a'))
print(w.search('.b'))
print(w.search('ab.'))
print(w.search('.'))
print(w.search('..'))
