# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self, letter: str = "", end: bool = False):
        self.letter = letter
        self.end = end
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode(word[i])
            curr = curr.children[word[i]]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.children:
                return False
            curr = curr.children[word[i]]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.children:
                return False
            curr = curr.children[prefix[i]]
        return True


t = Trie()
t.insert('abcd')
t.insert('abc')
print(t.search('abc'))
print(t.startsWith('abc'))
