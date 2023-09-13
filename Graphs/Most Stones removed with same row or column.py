from collections import defaultdict
class DisjointSet:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.size=[1]*(n+1)
        self.parent=[0]*(n+1)
        for i in range(n+1):
            self.parent[i]=i 
    
    def findUPar(self,node):
        if node==self.parent[node]:
            return node
        return self.findUPar(self.parent[node])
    
    def unionbyRank(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)
        if upl_u==ulp_v:
            return
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1   
            
    def unionbySize(self,u,v):
        ulp_u=self.findUPar(u)
        ulp_v=self.findUPar(v)
        if ulp_u==ulp_v:
            return
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        
        else:
            self.size[ulp_v]<self.size[ulp_u]
            self.parent[ulp_v]=ulp_u   
            self.size[ulp_u]+=self.size[ulp_v]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        mxr=0
        mxc=0
        for i in range(len(stones)):
            mxr=max(mxr,stones[i][0])
            mxc=max(mxc,stones[i][1])
        ds=DisjointSet(mxr+mxc+1)
        d=defaultdict(int)
        for i in stones:
            u=i[0]
            v=i[1]+mxr+1
            ds.unionbySize(u,v)
            d[u]=1
            d[v]=1
        c=0
        for key,value in d.items():
            if ds.parent[key]==key:
                c+=1 
        return len(stones)-c     
