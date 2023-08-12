class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n>=2**31:
            return -1
        nums=[]
        k=n
        while n!=0:
            d=n%10
            nums.insert(0,d)
            n=n//10
        i=len(nums)-1
        j=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i=i-1
        if i>0:
            while nums[j]<=nums[i-1]:
                j=j-1
            nums[i-1],nums[j]=nums[j],nums[i-1]
        nums[i:]=nums[i:][::-1]
        n=len(nums)-1
        s=0
        for i in range(len(nums)):
            s+=nums[i]*(10**n)
            n-=1
        if s>=2**31:
            return -1
        if s>k:
            return s
        else:
            return -1
        
