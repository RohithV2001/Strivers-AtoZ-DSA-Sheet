class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        a=0
        for i in nums:
            if i==1:
                c+=1
            else:
                c=0
            a=max(c,a)
        return a
            
