class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n=len(p)
        m=len(s)
        dp=[[False for _ in range(m+1)] for i in range(n+1)]
        dp[0][0]=True
        for i in range(1,m+1):
            dp[0][i]=False
        for i in range(n+1):
            flag=True
            for j in range(1,i+1):
                if p[j-1]!='*':
                    flag=False
            dp[i][0]=flag
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1]==s[j-1] or p[i-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[i-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        return dp[n][m]
                
