from typing import *

def superiorElements(a : List[int]) -> List[int]:
    l=[]
    n=len(a)
    l.append(a[n-1])
    mx=a[n-1]
    for i in range(n-2,-1,-1):
        if a[i]>mx:
            l.append(a[i])
            mx=a[i]
    return l
