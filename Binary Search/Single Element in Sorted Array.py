class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2
            if mid%2==0:
                if nums[mid]!=nums[mid+1]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]==nums[mid+1]:
                    high=mid-1
                else:
                    low=mid+1
        return nums[low]
