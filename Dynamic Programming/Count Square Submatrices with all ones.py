class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0 for _ in range(m)] for i in range(n)]
        for i in range(m):
            dp[0][i]=matrix[0][i]
        for j in range(n):
            dp[j][0]=matrix[j][0]
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    dp[i][j]=0
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        s=0
        for i in range(n):
            for j in range(m):
                s+=dp[i][j]
        return s
        
