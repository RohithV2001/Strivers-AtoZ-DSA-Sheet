class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=[]
        c1=0
        c2=0
        ele1=-1
        ele2=-1
        for i in nums:
            if ele1==i:
                c1+=1
            elif ele2==i:
                c2+=1
            elif c1==0:
                ele1=i
                c1=1
            elif c2==0:
                ele2=i
                c2=1
            else:
                c1-=1
                c2-=1
        c1=0
        c2=0
        for i in nums:
            if i==ele1:
                c1+=1
            elif i==ele2:
                c2+=1
        if c1>n//3:
            l.append(ele1)
        if c2>n//3:
            l.append(ele2)
        return l
