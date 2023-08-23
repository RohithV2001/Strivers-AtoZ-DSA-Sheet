class Solution:
    def jump(self, nums: List[int]) -> int:
        '''Using BFS consider nums = [2,3,1,1,4]
         BFS will be          2
                           3     1
                           1     4
        maintain two pointers l and r for finding the maximum for each level and update l,r accordingly'''
        l=0
        r=0
        ans=0
        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            ans+=1
        return ans
