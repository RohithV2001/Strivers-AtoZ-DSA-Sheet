class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]
        ds=[]
        def comb(idx,candidates,target,ds,l):
            if idx==len(candidates):
                if target==0:
                    l.append(list(ds))
                return
            if candidates[idx]<=target:
                ds.append(candidates[idx])
                comb(idx,candidates,target-candidates[idx],ds,l)
                ds.remove(ds[-1])
            comb(idx+1,candidates,target,ds,l)
        comb(0,candidates,target,ds,l)
        return l
