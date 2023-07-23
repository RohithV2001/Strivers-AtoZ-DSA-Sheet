class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        l=0
        h=(len(matrix[0])*len(matrix))-1
        while l<=h:
            m=(l+h)//2
            if matrix[m//(len(matrix[0]))][m%(len(matrix[0]))]== target:
                return True
            if matrix[m//(len(matrix[0]))][m%(len(matrix[0]))]<target:
                l=m+1
            else:
                h=m-1
        return False
