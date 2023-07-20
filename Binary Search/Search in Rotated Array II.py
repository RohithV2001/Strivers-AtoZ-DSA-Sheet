class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1:
            if nums[0]==target:
                return True
            else:
                return False
        low=0
        high=len(nums)-1
        while low<=high:
            while low<high and nums[low]==nums[low+1]:
                low+=1
            while low<high and nums[high]==nums[high-1]:
                high-=1
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[low]<=nums[mid]:
                if target>nums[mid] or target<nums[low]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if target<nums[mid] or target>nums[high]:
                    high=mid-1
                else:
                    low=mid+1
        return False
