from os import *
from sys import *
from collections import *
from math import *
class TrieNode:
    def __init__(self):
        self.data={}
        self.cp=0
        self.ce=0
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        node=self.root
        for i in word:
            if i not in node.data:
                node.data[i]=TrieNode()
            node=node.data[i]
            node
        node.ce+=1

    def countWordsEqualTo(self, word):
        node=self.root
        for i in word:
            if i  in node.data:
                node=node.data[i]
            else:
                return 0
        return node.ce

    def countWordsStartingWith(self, word):
        node=self.root
        for i in word:
            if i  in node.data:
                node=node.data[i]
            else:
                return 0
        return node.cp

    def erase(self, word):
        node=self.root
        for i in word:
            if i in node.data:
                node=node.data[i]
                node.cp-=1
            else:
                return 0
        node.ce-=1

