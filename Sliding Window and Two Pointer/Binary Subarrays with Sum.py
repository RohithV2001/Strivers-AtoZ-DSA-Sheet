class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(goal):
            if goal<0:
                return 0
            res=0
            l=0
            for r in range(len(nums)):
                goal-=nums[r]
                while goal<0:
                    goal+=nums[l]
                    l+=1
                res+=r-l+1
            return res
        return atmost(goal)-atmost(goal-1)
