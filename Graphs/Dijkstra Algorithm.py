class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        dist=[float('inf')]*V
        dist[S]=0
        q=[]
        q.append(S)
        while q:
            node=q.pop(0)
            for i in adj[node]:
                if dist[node]+i[1]<dist[i[0]]:
                    dist[i[0]]=i[1]+dist[node]
                    q.append(i[0])
        ans=[-1]*V
        for i in range(len(dist)):
            if dist[i]!=float('inf'):
                ans[i]=dist[i]
        return ans
