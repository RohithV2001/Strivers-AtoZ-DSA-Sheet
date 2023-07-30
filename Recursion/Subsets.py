class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''Using Recursion and Backtracking'''
        res=[]
        sub=[]
        def func(i):
            if i>=len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            func(i+1)
            sub.pop()
            func(i+1)
        func(0)
        return res

        '''Using Bit Manipulation'''
        res=[]
        res.append([])
        n=len(nums)
        for i in range(2**n):
            sub=[]
            for j in range(n):
                if (i & (1<<j))!=0:
                    sub.append(nums[j])
            if len(sub)>0:
                res.append(sub)
        return res'''
