class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row,col):
            self.vis[row][col]=1
            q=[]
            q.append([row,col])
            delrow=[-1,0,1,0]
            delcol=[0,1,0,-1]
            while q:
                ro,co=q.pop(0)
                for i in range(4):
                        nrow=ro+delrow[i]
                        ncol=co+delcol[i]
                        if nrow>=0 and nrow<self.n and ncol>=0 and ncol<self.m and self.grid[nrow][ncol]=='1' and self.vis[nrow][ncol]==0:
                            self.vis[nrow][ncol]=1
                            q.append([nrow,ncol])
        cnt=0
        self.grid=grid
        self.n=len(self.grid)
        self.m=len(self.grid[0])
        self.vis=[]
        for i in range(self.n):
            l=[0]*self.m
            self.vis.append(l)
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j]=='1' and self.vis[i][j]==0:
                    cnt+=1
                    bfs(i,j)
        return cnt
