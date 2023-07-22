def findPages(arr: [int], n: int, m: int) -> int:
    low=max(arr)
    high=sum(arr)
    if m>n:
        return -1
    def isPossible(arr,mid,m):
        c=1
        pages=0
        for i in range(len(arr)):
            if arr[i]+pages<=mid:
                pages+=arr[i]
            else:
                c+=1
                pages=arr[i]
        return c
    while low<=high:
        mid=(low+high)//2
        stu=isPossible(arr,mid,m)
        if stu>m:
            low=mid+1
        else:
            high=mid-1
    return low
