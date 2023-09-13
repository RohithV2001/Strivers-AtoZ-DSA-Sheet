class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        for i in times:
            adj[i[0]].append([i[1],i[2]])
        dist=[float('inf')]*(n+1)
        dist[k]=0
        q=[]
        q.append(k)
        cnt=0
        while q:
            node=q.pop(0)
            for i in adj[node]:
                if dist[node]+i[1]<dist[i[0]]:
                    dist[i[0]]=i[1]+dist[node]
                    q.append(i[0])
                    cnt+=1
        ans=[-1]*(n+1)
        ans[0]=-1
        dist[0]=-1
        for i in range(len(dist)):
            if dist[i]!=float('inf'):
                ans[i]=dist[i]
            else:
                return -1
        return max(ans)
        
