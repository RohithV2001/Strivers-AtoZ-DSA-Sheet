def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    def Ksorted(arr1,arr2,n,m,k):
        if n>m:
            return Ksorted(arr2,arr1,m,n,k)
        low=max(0,k-m)
        high=min(k,n)
        while low<=high:
            ct1=(low+high)>>1
            ct2=k-ct1
            l1=-1e6 if (ct1==0) else arr1[ct1-1]
            l2=-1e6 if (ct2==0) else arr2[ct2-1]
            r1=1e6 if (ct1==n) else arr1[ct1]
            r2=1e6 if (ct2==m) else arr2[ct2]
            if l1<=r2 and l2<=r1:
                return max(l1,l2)
            if l1>r2:
                high=ct1-1
            else:
                low=ct1+1
        return 1
    return Ksorted(arr1,arr2,n,m,k)
