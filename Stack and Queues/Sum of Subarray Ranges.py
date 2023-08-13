class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        arr=nums
        mnleftstack=[-1]*len(arr)
        mnrightstack=[len(arr)]*len(arr)
        mxleftstack=[-1]*len(arr)
        mxrightstack=[len(arr)]*len(arr)
        s=[]
        for i in range(len(arr)):
            while s and arr[s[-1]]>=arr[i]:
                idx=s.pop()
                mnrightstack[idx]=i
            s.append(i)
        s1=[]
        for i in range(len(arr)-1,-1,-1):
            while s1 and arr[s1[-1]]>arr[i]:
                idx=s1.pop()
                mnleftstack[idx]=i
            s1.append(i)
        s2=[]
        for i in range(len(arr)):
            while s2 and arr[s2[-1]]<=arr[i]:
                idx=s2.pop()
                mxrightstack[idx]=i
            s2.append(i)
        s3=[]
        for i in range(len(arr)-1,-1,-1):
            while s3 and arr[s3[-1]]<arr[i]:
                idx=s3.pop()
                mxleftstack[idx]=i
            s3.append(i)

        res=0
        for i in range(len(arr)):
            leftmin=i-mnleftstack[i]
            rightmin=mnrightstack[i]-i
            leftmx=i-mxleftstack[i]
            rightmx=mxrightstack[i]-i
            res+=arr[i]*(leftmx*rightmx-leftmin*rightmin)    
        return res
