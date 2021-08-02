class TrieNode:
    def __init__(self, file=None):
        self.children = {}
        self.file = file


class Files:
    def __init__(self):
        self.root = TrieNode()

    def listData(self, path):
        names = path.split('/')
        node = self.root
        for name in names:
            node = node.children[name]
        if node.file is not None:
            return [name]
        else:
            res = []
            children = sorted(node.children.keys())
            for child in children:
                res.append(child)
            return res

    def add(self, path):
        names = path.split('/')
        node = self.root
        for name in names:
            if name not in node.children:
                node.children[name] = TrieNode()
            node = node.children[name]

    def read(self, path):
        names = path.split('/')
        node = self.root
        for name in names:
            node = node.children[name]
        return node.file

    def appendData(self, path, data):
        names = path.split('/')
        node = self.root
        for name in names:
            if name not in node.children:
                node.children[name] = TrieNode()
            node = node.children[name]
        if node.file is None:
            node.file = ""
        node.file += data
