class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp = [[-1 for j in range(m)] for i in range(n)]
        '''
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0'''
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1 and i>=0 and j>=0:
                    dp[i][j]=0
                    continue
                if i==0 and j==0:
                    dp[i][j]=1
                    continue
                up=0
                left=0
                if i>0:
                    up = dp[i - 1][j]
                if j>0:
                    left = dp[i][j - 1]
                dp[i][j]=left+up
        return dp[n-1][m-1]

        
