lass Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def feasible(m):
            s=0
            for i in nums:
                s=s+ceil(i/m)
            return s<=threshold
        l=1
        h=max(nums)
        while l<h:
            m=l+(h-l)//2
            if feasible(m):
                h=m
            else:
                l=m+1
        return l
