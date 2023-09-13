class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.vis=[0]*n
        self.adj=[[] for _ in range(n)]
        for i in connections:
            self.adj[i[0]].append(i[1])
            self.adj[i[1]].append(i[0])
        self.tin=[0]*n
        self.low=[0]*n
        self.bridges=[]
        self.timer=1
        def dfs(node,parent):
            self.vis[node]=1
            self.tin[node]=self.timer
            self.low[node]=self.timer
            self.timer+=1
            for i in self.adj[node]:
                if i==parent:
                    continue
                if self.vis[i]==0:
                    dfs(i,node)
                    self.low[node]=min(self.low[node],self.low[i])
                    if self.low[i]>self.tin[node]:
                        self.bridges.append([i,node])
                else:
                    self.low[node]=min(self.low[node],self.low[i])
        dfs(0,-1)
        return self.bridges
        
