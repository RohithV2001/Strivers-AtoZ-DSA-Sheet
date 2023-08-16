class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        nums=list(s)
        k=3
        def atmost(k):
            d=collections.defaultdict(int)
            left=0
            ans=0
            for right,x in enumerate(nums):
                d[x]+=1
                while len(d)>k:
                    d[nums[left]]-=1
                    if d[nums[left]]==0:
                        del d[nums[left]]
                    left+=1
                ans+=right-left+1
            return ans
        return atmost(k)-atmost(k-1)
