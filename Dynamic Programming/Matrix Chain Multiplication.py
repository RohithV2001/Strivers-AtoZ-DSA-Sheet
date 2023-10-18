import sys
from sys import stdin

def calculate(p,i,j,dp):
    if i==j:
        return 0
        '''
    if dp[i][j]!=-1:
        return dp[i][j]'''
    mini=int(1e9)
    for k in range(i,j):
        steps=calculate(p,i,k,dp)+calculate(p,k+1,j,dp)+p[i-1]*p[k]*p[j]
        mini=min(mini,steps)
    #dp[i][j]=mini
    return mini




def mcm(p,n):
    arr=p
    N=n
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    # Initialize the diagonal elements of the dp table to 0
    for i in range(N):
        dp[i][i] = 0
    
    # Loop through the dp table to calculate the minimum number of operations
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            mini = float('inf')
            
            # Partitioning loop
            for k in range(i, j):
                ans = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                mini = min(mini, ans)
            
            dp[i][j] = mini
    
    # The result is stored in the top-right corner of the dp table
    return dp[0][N - 1]
    '''
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i]=0
    for i in range(n-1,0,-1):
        for j in range(i+1,n):
            mini=int(1e9)
            for k in range(i,j):
                res=dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]
                mini=min(res,mini)
            dp[i][j]=mini
    return dp[1][n-1]'''
    








n=int(stdin.readline().strip())
p=[int(i) for i in stdin.readline().strip().split()]
print(mcm(p,n))
