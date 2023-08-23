#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        res=1
        pf=1
        arr.sort()
        dep.sort()
        i=1
        j=0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                pf+=1
                i+=1
            elif arr[i]>dep[j]:
                pf-=1
                j+=1
            if pf>res:
                res=pf
        return res
        
