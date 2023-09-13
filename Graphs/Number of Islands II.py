#User function Template for python3
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



from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        ds=DisjointSet(n*m)
        visit=[]
        for i in range(rows):
            l=[0]*cols
            visit.append(l)
        cnt=0
        ans=[]
        for i in operators:
            row=i[0]
            col=i[1]
            if visit[row][col]==1:
                ans.append(cnt)
                continue
            visit[row][col]=1
            cnt+=1
            delrow=[-1,0,1,0]
            delcol=[0,1,0,-1]
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<rows and ncol>=0 and ncol<cols:
                    if visit[nrow][ncol]==1:
                        nodeno=row*m+col
                        adjnode=nrow*m+ncol
                        if ds.findUPar(nodeno)!=ds.findUPar(adjnode):
                            cnt-=1
                            ds.unionbySize(nodeno,adjnode)
            ans.append(cnt)
        return ans
                        





























