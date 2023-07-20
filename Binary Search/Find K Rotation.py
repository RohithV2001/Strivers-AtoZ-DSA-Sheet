def findKRotation(arr : [int]) -> int:
    low=0
    high=len(arr)-1
    ans=999999999999
    idx=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            if arr[low]<ans:
                idx=low
                ans=arr[low]
            break
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                idx=low
                ans=arr[low]
            low=mid+1
        else:
            if arr[mid]<ans:
                idx=mid
                ans=arr[mid]
            high=mid-1
    return idx
