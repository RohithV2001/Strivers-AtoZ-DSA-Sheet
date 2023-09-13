#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        self.adj=adj
        self.vis=[0]*V
        self.pathvis=[0]*V
        def dfs(node):
            self.vis[node]=1
            self.pathvis[node]=1
            for i in self.adj[node]:
                if self.vis[i]==False:
                    if dfs(i)==True:
                        return True
                elif self.pathvis[i]==1:
                    return True
            self.pathvis[node]=0
            return False
        for i in range(V):
           if self.vis[i]==0:
               if dfs(i)==True:
                   return True
        return False
        
        
                        
