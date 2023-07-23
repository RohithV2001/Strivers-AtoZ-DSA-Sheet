class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        #Followed the hint
        m,n=len(mat),len(mat[0])
        l=0
        r=n
        mx=0
        left=False
        while l<=r:
            mid=(l+r)//2
            for i in range(m):
                if i>0 and mat[i-1][mid]>=mat[i][mid]:
                    continue
                if i+1<m and mat[i+1][mid]>=mat[i][mid]:
                    continue
                if mid+1<n and mat[i][mid+1]>=mat[i][mid]:
                    left=False
                    continue
                if mid>0 and mat[i][mid-1]>=mat[i][mid]:
                    left=True
                    continue
                return [i,mid]
            if left:
                r=mid-1
            else:
                l=mid+1
        return []
