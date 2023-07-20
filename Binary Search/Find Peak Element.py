class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r-1:
            mid=(l+r)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid-1
        return l if nums[l]>=nums[r] else r
