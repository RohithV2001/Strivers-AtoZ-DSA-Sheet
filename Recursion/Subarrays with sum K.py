def subarraysWithSumK( a:[int], k:int) ->[[int]]:
    def subarray(a,k):
        start=0
        end=0
        n=len(a)
        cs=0
        res=[]
        while end<n:
            cs+=a[end]
            while cs>k and start<=end:
                cs-=a[start]
                start+=1
            if cs==k:
                res.append(a[start:end+1])
                cs-=a[start]
                start+=1
            end+=1
        return res
    return subarray(a,k)
