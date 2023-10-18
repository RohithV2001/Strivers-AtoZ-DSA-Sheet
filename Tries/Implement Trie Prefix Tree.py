class TrieNode:
    def __init__(self):
        self.flag=False
        self.data={}
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for i in word:
            if i not in node.data:
                node.data[i]=TrieNode()
            node=node.data[i]
        node.flag=True

    def search(self, word: str) -> bool:
        node=self.root
        for i in word:
            if i not in node.data:
                return False
            node=node.data[i]
        return node.flag

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for i in prefix:
            if i not in node.data:
                return False
            node=node.data[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
