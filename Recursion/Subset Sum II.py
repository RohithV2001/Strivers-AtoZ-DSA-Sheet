class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds=[]
        l=[]
        nums.sort()
        def subset(idx,nums,ds,l):
            l.append(list(ds))
            for i in range(idx,len(nums)):
                if i!=idx and nums[i]==nums[i-1]:
                    continue
                ds.append(nums[i])
                subset(i+1,nums,ds,l)
                ds.remove(ds[len(ds)-1])
        subset(0,nums,ds,l)
        return l
