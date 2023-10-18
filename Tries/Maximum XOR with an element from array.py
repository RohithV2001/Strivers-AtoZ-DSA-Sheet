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



class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        ans=[-1]*len(queries)
        oq=[]
        idx=0
        for query in queries:
            oq.append([query[1],[query[0],idx]])
            idx+=1
        oq.sort()
        i=0
        n=len(nums)
        res=Trie()
        for que in oq:
            while i<n and nums[i]<=que[0]:
                res.insert(nums[i])
                i+=1
            idx=que[1][1]
            num=que[1][0]
            if i!=0:
                ans[idx]=res.getmax(num)
        return ans





