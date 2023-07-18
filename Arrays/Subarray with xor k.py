from collections import defaultdict
def subarraysWithSumK(a: [int], b: int) -> int:
    xr=0
    c=0
    d=defaultdict(int)
    d[xr]=1
    for i in range(len(a)):
        xr=xr^a[i]
        x=xr^b
        c+=d[x]
        d[xr]+=1
    return c
