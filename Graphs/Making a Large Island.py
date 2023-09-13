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
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ds=DisjointSet(n*n)
        for row in range(n):
            for col in range(n):
                if grid[row][col]==0:
                    continue
                delrow=[-1,0,1,0]
                delcol=[0,-1,0,1]
                for i in range(4):
                    nrow=row+delrow[i]
                    ncol=col+delcol[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                        nodeno=row*n+col
                        adjno=nrow*n+ncol
                        ds.unionbySize(nodeno,adjno)
        mx=0
        for row in range(n):
            for col in range(n):
                if grid[row][col]==1:
                    continue
                s=set()
                delrow=[-1,0,1,0]
                delcol=[0,-1,0,1]
                for i in range(4):
                    nrow=row+delrow[i]
                    ncol=col+delcol[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                        s.add(ds.findUPar(nrow*n+ncol))
                size=0
                for i in s:
                    size+=ds.size[i]
                mx=max(mx,size+1)
        for i in range(n*n):
            mx=max(mx,ds.size[ds.findUPar(i)])
        return mx
        
