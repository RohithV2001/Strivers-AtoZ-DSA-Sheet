class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        s=sum(nums)
        if s%2==1:
            return False
        else:
            k=s//2
            prev=[False]*(k+1)
            prev[0]=True
            if nums[0]<=k:
                prev[nums[0]]=True
            for i in range(1,n):
                cur=[False]*(k+1)
                cur[0]=True
                for t in range(1,k+1):
                    nottaken=prev[t]
                    taken=False
                    if nums[i]<=k:
                        taken=prev[t-nums[i]]
                    cur[t]=taken or nottaken
                prev=cur
        return prev[k]
        
        
