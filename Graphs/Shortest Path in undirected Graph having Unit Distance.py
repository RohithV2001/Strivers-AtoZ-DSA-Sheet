#User function Template for python3

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj=[[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        dist=[float('inf')]*n
        dist[src]=0
        q=[]
        q.append(src)
        while q:
            node=q.pop(0)
            for i in adj[node]:
                if dist[node]+1<dist[i]:
                    dist[i]=1+dist[node]
                    q.append(i)
        ans=[-1]*n
        for i in range(len(dist)):
            if dist[i]!=float('inf'):
                ans[i]=dist[i]
        return ans
