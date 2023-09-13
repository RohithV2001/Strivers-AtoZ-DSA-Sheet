#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        self.vis=[0]*V
        self.low=[0]*V
        self.tin=[0]*V
        self.mark=[0]*V
        self.timer=1
        def dfs(node,parent):
            self.vis[node]=1
            self.tin[node]=self.timer
            self.low[node]=self.timer
            self.timer+=1
            child=0
            for i in adj[node]:
                if i==parent:
                    continue
                if self.vis[i]==0:
                    dfs(i,node)
                    self.low[node]=min(self.low[node],self.low[i])
                    if self.low[i]>=self.tin[node] and parent!=-1:
                        self.mark[node]=1
                    child+=1
                else:
                    self.low[node]=min(self.low[node],self.tin[i])
            if child>1 and parent==-1:
                self.mark[node]=1
                        
        for i in range(V):
            if self.vis[i]==0:
                dfs(0,-1)
                
        ans=[]
        for i in range(V):
            if self.mark[i]==1:
                ans.append(i)
        if len(ans)==0:
            ans.append(-1)
        return ans
        
