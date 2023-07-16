class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        st=set(nums)
        ls=0
        cs=0
        cn=0
        for i in nums:
            if i-1 not in st:
                cn=i
                cs=1
                while cn+1 in st:
                    cn+=1
                    cs+=1
                ls=max(ls,cs)
        return ls
