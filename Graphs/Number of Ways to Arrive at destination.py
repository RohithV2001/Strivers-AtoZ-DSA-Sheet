import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(src):
            dist = [math.inf] * n
            ways = [0] * n
            minHeap = [(0, src)]  # dist, src
            dist[src] = 0
            ways[src] = 1
            while minHeap:
                d, u = heappop(minHeap)
                if dist[u] < d: continue  # Skip if `d` is not updated to latest version!
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heappush(minHeap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)
        '''
        adj=[[] for _ in range(n)]
        dist=[float('inf')]*n
        ways=[0]*n
        for i in roads:
            adj[i[0]].append([i[1],i[2]])
            adj[i[1]].append([i[0],i[2]])
        dist[0]=0
        ways[0]=1
        mod=((10**9)+7)
        q=[]
        heapq.heappush(q,[0,0])
        while q:
            node,d=heapq.heappop(q)
            for i in adj[node]:
                if i[1]+d<dist[i[0]]:
                    dist[i[0]]=i[1]+d
                    ways[i[0]]=ways[node]
                    heapq.heappush(q,[i[0],d+i[1]])
                elif i[1]+d==dist[i[0]]:
                    ways[i[0]]=((ways[node])%mod+(ways[i[0]])%mod)%(mod)
        return (ways[n-1])%mod
        '''
