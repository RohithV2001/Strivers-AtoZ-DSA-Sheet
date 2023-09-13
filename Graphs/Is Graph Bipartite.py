class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.graph=graph
        self.n=len(self.graph)
        self.vis=[-1]*self.n
        def dfs(node,col):
            self.vis[node]=col
            for i in self.graph[node]:
                if self.vis[i]==-1:
                    if dfs(i,1-col)==False:
                        return False
                elif self.vis[i]==col:
                    return False
            return True

        for i in range(self.n):
            if self.vis[i]==-1:
                if dfs(i,0)==False:
                    return False
        return True
