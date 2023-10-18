class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s=sum(nums)
        if s-target<0 or (s-target)%2:
            return 0
        k=(s-target)//2
        prev=[]
        for i in range(k+1):
            prev.append(0)
        if nums[0]==0:
            prev[0]=2
        else:
            prev[0]=1
        if nums[0]!=0 and nums[0]<=k:
            p=nums[0]
            prev[p]=1
        for i in range(1,n):
            cur=[0]*(k+1)
            for j in range(k+1):
                notTaken=prev[j]
                taken=0
                if nums[i]<=j:
                    taken=prev[j-nums[i]]
                cur[j]=taken+notTaken
            prev=cur
        return prev[k]
        
