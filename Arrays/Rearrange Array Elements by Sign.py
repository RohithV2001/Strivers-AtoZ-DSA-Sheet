class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nw=[0]*len(nums)
        i=0
        j=1
        for n in nums:
            if n>0:
                nw[i]=n
                i=i+2
            else:
                nw[j]=n
                j=j+2
        return nw
