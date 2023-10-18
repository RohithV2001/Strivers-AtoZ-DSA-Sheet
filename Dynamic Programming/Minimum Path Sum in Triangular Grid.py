class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        front=[0]*n
        cur=[0]*n
        for i in range(n):
            front[i]=triangle[n-1][i]
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                down=triangle[i][j]+front[j]
                diag=triangle[i][j]+front[j+1]
                cur[j]=min(down,diag)
            front=cur
        return front[0]
