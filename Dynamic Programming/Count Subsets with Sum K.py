from typing import List

def findWays(arr: List[int], k: int) -> int:
    n=len(arr)
    mod=(int(1e9)+7)
    prev=[0 for i in range(k + 1)]
    prev[0]=1
    if arr[0]<=k:
        prev[arr[0]]=1
    for i in range(1,n):
        cur=[0 for i in range(k + 1)]
        cur[0]=1
        for t in range(1,k+1):
            nottaken=prev[t]
            taken=0
            if arr[i]<=t:
                taken=prev[t-arr[i]]
            cur[t]=taken+nottaken
        prev=cur
    return prev[k]%mod
