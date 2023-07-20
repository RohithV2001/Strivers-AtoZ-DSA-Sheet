from math import *

def ceilingInSortedArray(n, x, arr):
    arr.sort()
    low=0
    high=n-1
    ans1=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=x:
            ans1=arr[mid]
            low=mid+1
        else:
            high=mid-1
    low=0
    high=n-1
    ans2=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans2=arr[mid]
            high=mid-1
        else:
            low=mid+1
    print(ans1, ans2)
