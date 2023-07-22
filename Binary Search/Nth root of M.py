from sys import *
from collections import *
from math import *
def func(mid,n,m):
    ans=1
    for i in range(1,n+1):
        ans=ans*mid
        if ans>m:
            return 2
    if ans==m:
        return 1
    else:
        return 0

def findNthRootOfM(n,m):
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        x=func(mid,n,m)
        if x==1:
            return mid    
        if x==2:
            high=mid-1
        else:
            low=mid+1
    return -1
