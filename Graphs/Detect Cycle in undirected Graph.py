from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        self.adj=adj
        def checkcycle(root):
            q=[]
            self.vis[root]=True
            q.append([root,-1])
            while q:
                node,par=q.pop(0)
                for i in self.adj[node]:
                    if self.vis[i]==False:
                        self.vis[i]=True
                        q.append([i,node])
                    elif par!=i:
                        return True
            return False
        self.vis=[False]*V
        for i in range(V):
            if self.vis[i]==False:
                if checkcycle(i):
                    return True
        return False
