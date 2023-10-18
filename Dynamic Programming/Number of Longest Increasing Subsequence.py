class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1 for _ in range(n)]
        ct=[1 for _ in range(n)]
        maxi=0
        for i in range(n):
            for prev in range(i):
                if nums[i]>nums[prev] and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    ct[i]=ct[prev]
                elif nums[i]>nums[prev] and 1+dp[prev]==dp[i]:
                    ct[i]+=ct[prev]
            maxi=max(maxi,dp[i])
        count=0
        for i in range(n):
            if dp[i]==maxi:
                count+=ct[i]
        return count

        
