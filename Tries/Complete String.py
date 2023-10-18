from os import *
from sys import *
from collections import *
from math import *

from typing import *
class TrieNode:
    def __init__(self):
        self.data={}
        self.flag=False
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
        node.flag=True
        node.ce+=1


    def searchprefix(self, word):
        node=self.root
        for i in word:
            if i in node.data:
                node=node.data[i]
            else:
                return False
        if node.ce>0:
            return True

    

def completeString(n: int, a: List[str])-> str:
    l=[]
    sol=Trie()
    val=TrieNode()
    for i in a:
        sol.insert(i)
    lon=""
    for st in a:
        c=0
        for i in range(len(st)):
            if sol.searchprefix(st[:i+1])==True:
                c+=1
            else:
                break
        if c==len(st):
            if c>len(lon):
                lon=st
            elif c==len(lon) and st<lon:
                lon=st
    if lon=="":
        return None
    return lon

