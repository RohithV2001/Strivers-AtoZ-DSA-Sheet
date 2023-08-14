class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
             return [max(nums)]
        i,j=0,0
        l=[]
        ans=[]
        while j<len(nums):
            while len(l)>0 and l[-1]<nums[j]:
                l.pop()
            l.append(nums[j])
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                ans.append(l[0])
                if l[0]==nums[i]:
                    l.pop(0)
                i+=1
                j+=1
        return ans
