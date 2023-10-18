class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        prev=[0]*m
        cur=[0]*m
        for i in range(m):
            prev[i]=matrix[0][i]
        for i in range(1,n):
            for j in range(m):
                up=matrix[i][j]+prev[j]
                left=matrix[i][j]
                if j-1>=0:
                    left+=prev[j-1]
                else:
                    left+=int(1e9)
                right=matrix[i][j]
                if j+1<m:
                    right+=prev[j+1]
                else:
                    right+=int(1e9)
                cur[j]=min(min(left,right),up)
            prev=cur[:]
        mini=int(1e9)
        for i in range(m):
            mini=min(mini,prev[i])
        return mini
