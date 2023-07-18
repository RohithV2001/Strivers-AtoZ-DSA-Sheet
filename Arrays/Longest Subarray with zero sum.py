from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    d={}
    mx=0
    s=0
    for i in range(len(arr)):
        s+=arr[i]
        if s==0:
            mx=i+1
        if s not in d:
            d[s]=i
        else:
            mx=max(i-d[s],mx)
    return mx
