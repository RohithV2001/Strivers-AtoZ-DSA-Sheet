class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=nums[0]
        ms=nums[0]
        for i in range(1,len(nums)):
            if cs>0:
                cs=cs+nums[i]
            else:
                cs=nums[i]
            ms=max(ms,cs)
        return ms
