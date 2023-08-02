#User function Template for python3

class Solution:
    def findPath(self, m, n):
        s=""
        ans=[]
        vis = []
        for i in range(n):
            vis.append([])
            for j in range(n):
                vis[i].append(0)
        def solve(i,j,ans,s,vis,m,n):
            if i==n-1 and j==n-1:
                ans.append(s)
                return
            if i+1<n and m[i+1][j]==1 and vis[i+1][j]==0:
                vis[i][j]=1
                solve(i+1,j,ans,s+'D',vis,m,n)
                vis[i][j]=0
            if j-1>=0  and m[i][j-1]==1 and vis[i][j-1]==0:
                vis[i][j]=1
                solve(i,j-1,ans,s+'L',vis,m,n)
                vis[i][j]=0
            if j+1<n and m[i][j+1]==1 and vis[i][j+1]==0:
                vis[i][j]=1
                solve(i,j+1,ans,s+'R',vis,m,n)
                vis[i][j]=0
            if i-1>=0 and m[i-1][j]==1 and vis[i-1][j]==0:
                vis[i][j]=1
                solve(i-1,j,ans,s+'U',vis,m,n)
                vis[i][j]=0
        if m[0][0]==1:
            solve(0,0,ans,s,vis,m,n)
            return ans
        else:
            return ans
                
                
