class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        dist=[float('inf')]*n
        for i in flights:
            adj[i[0]].append([i[1],i[2]])
        q=[]
        q.append([0,src,0])
        while q:
            s,node,d=q.pop(0)
            if s>k:
                continue
            for i in adj[node]:
                if d+i[1]<dist[i[0]]:
                    dist[i[0]]=d+i[1]
                    q.append([s+1,i[0],d+i[1]])
        if dist[dst]!=float('inf'):
            return dist[dst]
        return -1
