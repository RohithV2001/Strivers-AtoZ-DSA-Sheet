from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adj=defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]!=0 and i!=j:
                    self.adj[i].append(j)
                    self.adj[j].append(i)
        V=len(isConnected)
        self.vis=[0]*V
        def dfs(node):
            self.vis[node]=1
            for i in self.adj[node]:
                if self.vis[i]==0:
                    dfs(i)
        cnt=0
        for i in range(V):
            if self.vis[i]==0:
                cnt+=1
                dfs(i)
        return cnt
        
