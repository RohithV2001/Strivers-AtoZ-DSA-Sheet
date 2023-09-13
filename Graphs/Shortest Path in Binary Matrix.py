class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        src=[0,0]
        if grid[src[0]][src[1]]==1 or (len(grid)<2 and grid[src[0]][src[1]]==1):
            return -1

        n=len(grid)
        dest=[n-1,n-1]
        if src[0]==dest[0] and src[1]==dest[1]:
            return 1
        dist=[]
        for i in range(n):
            l=[float('inf')]*n
            dist.append(l)
        dist[src[0]][src[1]]=0
        q=[]
        q.append([1,src[0],src[1]])
        while q:
            d,r,c=q.pop(0)
            for i in range(-1,2):
                for j in range(-1,2):
                    nrow=r+i
                    ncol=c+j
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==0 and d+1<dist[nrow][ncol]:
                        dist[nrow][ncol]=d+1
                        if nrow==dest[0] and ncol==dest[1]:
                            return d+1
                        q.append([d+1,nrow,ncol])
        return -1 
