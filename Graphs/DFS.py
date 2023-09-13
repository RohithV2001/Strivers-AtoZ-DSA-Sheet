#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        self.adj=adj
        self.vis=[0]*V
        self.l=[]
        def dfs(node):
            self.vis[node]=1
            self.l.append(node)
            for i in self.adj[node]:
                if self.vis[i]!=1:
                    dfs(i)
        self.vis[0]=1
        dfs(0)
        return self.l
        
