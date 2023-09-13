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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        ds=DisjointSet(n)
        d={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in d:
                    d[mail]=i
                else:
                    ds.unionbySize(i,d[mail])
        mergedmail=[[] for _ in range(n)]
        for mail,value in d.items():
            node=ds.findUPar(value)
            mergedmail[node].append(mail)
        ans=[]
        for i in range(n):
            if len(mergedmail[i])==0:
                continue
            mergedmail[i].sort()
            temp=[]
            temp.append(accounts[i][0])
            for node in mergedmail[i]:
                temp.append(node)
            ans.append(temp) 

        return ans 
