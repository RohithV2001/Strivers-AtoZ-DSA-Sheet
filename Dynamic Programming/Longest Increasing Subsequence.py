from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        temp=[]
        temp.append(nums[0])
        l=1
        for i in range(1,n):
            if nums[i]>temp[l-1]:
                temp.append(nums[i])
                l+=1
            else:
                k=bisect_left(temp,nums[i])
                temp[k]=nums[i]
        return l
        
