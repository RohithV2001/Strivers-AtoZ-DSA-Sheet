class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        h=sum(nums)
        if k>len(nums):
            return -1
        def pos(A,mid,M):
            c=1
            p=0
            for i in range(len(A)):
                if A[i]+p<=mid:
                    p+=A[i]
                else:
                    c+=1
                    p=A[i]
            return c
        while l<=h:
            m=(l+h)>>1
            part=pos(nums,m,k)
            if part>k:
                l=m+1
            else:
                h=m-1
        return l
