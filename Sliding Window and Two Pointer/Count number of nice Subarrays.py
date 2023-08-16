class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            if k<0:
                return 0
            res=0
            l=0
            for r in range(len(nums)):
                if nums[r]%2!=0:
                    k-=1
                while k<0:
                    k+=nums[l]%2
                    l+=1
                res=res+r-l+1
            return res
        return atmost(k)-atmost(k-1)
