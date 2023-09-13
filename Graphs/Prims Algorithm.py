#User function Template for python3
from heapq import heappop,heappush
from collections import defaultdict
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        graph = defaultdict(list)
        for index, val in enumerate(adj):
            for arrs in val:
                graph[index].append((arrs[0], arrs[1]))
        
        seen = set()
        heap = [(0, 0)]  # pair of (dist, vertex)
        mincost = 0
        
        while len(seen) < V:
            dist, u = heappop(heap)
            if u in seen: continue
            seen.add(u)
            mincost += dist
            for v, d in graph[u]:
                if v not in seen:
                    heappush(heap, (d, v))
        return mincost
        '''
        vis=[0]*V
        q=[]
        heapq.heappush(q,[0,0])
        s=0
        while q:
            node,wt=heapq.heappop(q)
            if vis[node]==1:
                continue
            vis[node]=1
            s=s+wt
            for i in graph[node]:
                val=i[0]
                wg=i[1]
                if vis[val]==0:
                    heapq.heappush(q,[val,wg])
        return s   '''                    
