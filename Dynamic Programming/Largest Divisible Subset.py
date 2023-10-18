class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dp=[1 for _ in range(n)]
        hash=list(range(n))
        nums.sort()
        for i in range(n):
            for prev in range(i):
                if nums[i]%nums[prev]==0 and dp[prev]+1>dp[i]:
                    dp[i]=1+dp[prev]
                    hash[i]=prev
        li=-1
        ans=-1
        for i in range(n):
            if dp[i]>ans:
                ans=dp[i]
                li=i
        res=[nums[li]]
        while hash[li]!=li:
            li=hash[li]
            res.append(nums[li])
        return res

        
