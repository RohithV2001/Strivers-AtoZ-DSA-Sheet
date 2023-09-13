import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        dist=[]
        for i in range(n):
            l=[float('inf')]*m
            dist.append(l)
        dist[0][0]=0
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        ne=999999
        q=[]
        heapq.heappush(q,[0,0,0])
        while q:
            d,r,c=heapq.heappop(q)
            if r==n-1 and c==m-1:
                return d
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                    ne=max(abs(heights[nrow][ncol]-heights[r][c]),d)
                    if ne<dist[nrow][ncol]:
                        dist[nrow][ncol]=ne
                        heapq.heappush(q,[ne,nrow,ncol])
        return 0
