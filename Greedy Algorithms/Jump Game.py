class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''Traverse from back to find the if goal is suitable for all integers'''
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal:
                goal=i
        if goal==0:
            return True
        return False
