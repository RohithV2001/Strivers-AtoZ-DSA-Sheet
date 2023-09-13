class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''Using DP'''
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat
        '''
        vis=[]
        for i in range(len(mat)):
            k=[0]*len(mat[0])
            vis.append(k)
        q=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    vis[i][j]=1
        dist=[]
        for i in range(len(mat)):
            k=[0]*len(mat[0])
            dist.append(k)
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        while q:
            row,col,space=q.pop(0)
            dist[row][col]=space
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<len(mat) and ncol>=0 and ncol<len(mat[0]) and vis[nrow][ncol]==0:
                    vis[nrow][ncol]=1
                    q.append([nrow,ncol,space+1])
        return dist'''

        
