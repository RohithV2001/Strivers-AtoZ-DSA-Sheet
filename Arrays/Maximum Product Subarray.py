class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx_prod=nums[0]
        mn_prod=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            x=max(nums[i],mx_prod*nums[i],mn_prod*nums[i])
            y=min(nums[i],mx_prod*nums[i],mn_prod*nums[i])
            mx_prod=x
            mn_prod=y
            ans=max(ans,mx_prod)
        return ans
