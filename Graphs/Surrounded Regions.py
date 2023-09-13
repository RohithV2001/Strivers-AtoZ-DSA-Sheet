class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board=board
        self.vis=[]
        self.n=len(board)
        self.m=len(board[0])
        for i in range(self.n):
            k=[0]*self.m
            self.vis.append(k)
        def dfs(row,col):
            self.vis[row][col]=1
            for i in range(4):
                nrow=row+self.delrow[i]
                ncol=col+self.delcol[i]
                if nrow>=0 and nrow<self.n and ncol>=0 and ncol<self.m and self.vis[nrow][ncol]==0 and self.board[nrow][ncol]=='O':
                    dfs(nrow,ncol)

        self.delrow=[-1,0,1,0]
        self.delcol=[0,1,0,-1]
        for j in range(self.m):
            if self.vis[0][j]==0 and self.board[0][j]=='O':
                dfs(0,j)
            if self.vis[self.n-1][j]==0 and self.board[self.n-1][j]=='O':
                dfs(self.n-1,j)
        for i in range(self.n):
            if self.vis[i][0]==0 and self.board[i][0]=='O':
                dfs(i,0)
            if self.vis[i][self.m-1]==0 and self.board[i][self.m-1]=='O':
                dfs(i,self.m-1)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j]=='O' and self.vis[i][j]==0:
                    self.board[i][j]='X'

        return self.board
