class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        leftstack=[-1]*len(arr)
        rightstack=[len(arr)]*len(arr)
        s=[]
        for i in range(len(arr)):
            while s and arr[s[-1]]>=arr[i]:
                idx=s.pop()
                rightstack[idx]=i
            s.append(i)
        s1=[]
        for i in range(len(arr)-1,-1,-1):
            while s1 and arr[s1[-1]]>arr[i]:
                idx=s1.pop()
                leftstack[idx]=i
            s1.append(i)
        res=0
        for i in range(len(arr)):
            a=i-leftstack[i]
            b=rightstack[i]-i
            res+=arr[i]*a*b
            
        return res % (10**9 + 7)
