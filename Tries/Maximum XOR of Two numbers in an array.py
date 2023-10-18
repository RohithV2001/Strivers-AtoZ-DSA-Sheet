
'''
class TrieNode:
    def __init__(self):
        self.data={}
        self.flag=False
class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self,num ):
        node=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if bit not in node.data:
                node.data[bit]=TrieNode()
            node=node.data[bit]
        node.flag=True

    def getmax(self,num):
        node=self.root
        mxnum=0
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if 1-bit in node.data:
                mxnum=mxnum | (1<<i)
                node=node.data[1-bit]
            else:
                node=node.data[bit]
        return mxnum
'''
class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]
                
    def query(self, num):
        if not self.root: 
            return -1
        p, ans = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                ans |= (1 << i)
            else:
                p = p[cur]
        return ans
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        sol=Trie()
        n=len(nums)
        for i in range(n):
            sol.insert(nums[i])
        maxi=0
        for i in range(n):
            maxi=max(maxi,sol.query(nums[i]))
        return maxi
