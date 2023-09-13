#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append([i[1],i[2]])
        dist=[float('inf')]*n
        dist[0]=0
        q=[]
        q.append(0)
        while q:
            node=q.pop(0)
            for i in adj[node]:
                if dist[node]+i[1]<dist[i[0]]:
                    dist[i[0]]=i[1]+dist[node]
                    q.append(i[0])
        ans=[-1]*n
        for i in range(len(dist)):
            if dist[i]!=float('inf'):
                ans[i]=dist[i]
        return ans
