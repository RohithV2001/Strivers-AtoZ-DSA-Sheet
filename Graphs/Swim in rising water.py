class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=n
        dist=[]
        res=0
        for i in range(n):
            l=[float('inf')]*m
            dist.append(l)
        dist[0][0]=0
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        ne=0
        q=[]
        heapq.heappush(q,[grid[0][0],0,0])
        while q:
            d,r,c=heapq.heappop(q)
            res=max(res,d)
            if r==n-1 and c==m-1:
                return res
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                    #ne=max(abs(grid[nrow][ncol]-grid[r][c]),d)
                    if dist[nrow][ncol]==float('inf'):
                        dist[nrow][ncol]=1
                        heapq.heappush(q,[grid[nrow][ncol],nrow,ncol])
        #return 0
        
