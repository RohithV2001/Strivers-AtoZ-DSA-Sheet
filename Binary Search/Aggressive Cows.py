def aggressiveCows(stalls, k):
    stalls.sort()
    low=0
    high=stalls[len(stalls)-1]-stalls[0]
    def isPossible(arr,cows,mid):
        c=1
        st=arr[0]
        for i in range(1,len(arr)):
            if arr[i]-st>=mid:
                c+=1
                st=arr[i]
            if c>=cows:
                return True
        return False
    while low<=high:
        mid=(low+high)//2
        if isPossible(stalls,k,mid):
            res=mid
            low=mid+1
        else:
            high=mid-1
    return high
