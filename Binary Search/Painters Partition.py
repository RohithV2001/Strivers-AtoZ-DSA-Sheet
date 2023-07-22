def findLargestMinDistance(boards:list, k:int):
    low=max(boards)
    high=sum(boards)
    def isPossible(arr,mid,k):
        c=1
        p=0
        for i in range(len(arr)):
            if arr[i]+p<=mid:
                p+=arr[i]
            else:
                c+=1
                p=arr[i]
        return c
    while low<=high:
        mid=(low+high)//2
        paint=isPossible(boards,mid,k)
        if paint>k:
            low=mid+1
        else:
            high=mid-1
    return low
